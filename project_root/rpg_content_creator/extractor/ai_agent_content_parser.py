from shared.models.entities import Character, SessionLocal  # Ensure the correct import
from sqlalchemy.orm import Session
import fitz  # PyMuPDF
import spacy
import random
from collections import Counter
import logging
import requests

from .settings import get_setting, get_ollama_settings  # Ensure correct imports
from app import db  # Use the Flask-SQLAlchemy db object

logger = logging.getLogger('app')

# Load spaCy model
nlp = spacy.load("en_core_web_sm")
nlp.max_length = 2000000

def generate_content(prompt: str, ollama_url: str, ollama_model: str, temperature: float = 0.8) -> str:
    try:
        response = requests.post(
            f"{ollama_url}/api/generate",
            json={"model": ollama_model, "prompt": prompt, "temperature": temperature, "stream": False}
        )
        response.raise_for_status()
        return response.json().get("response", "")
    except Exception as e:
        print(f"Error generating content: {e}")
        return "Sorry, I couldn't process that request."

def extract_text_from_pdf(pdf_content):
    doc = fitz.open(stream=pdf_content, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def extract_names(text):
    doc = nlp(text)
    names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
    return names

def consolidate_names(names):
    name_counts = Counter(names)
    common_names = [name for name, count in name_counts.items() if count > 1]
    return common_names

def generate_character_details(name, ollama_url, ollama_model):
    prompt = f"Provide a detailed description for the character {name} including their name, sex, age, traits, behaviors, a brief background summary, and some dialogue examples in bullet points."
    details = generate_content(prompt, ollama_url, ollama_model, temperature=0.8)
    logger.debug(f"Generated character details for {name}: {details}")
    return details

def generate_book_details(text, db, ollama_url, ollama_model):
    prompt = f"Provide the book title, author, and genre of the following text: {text}"
    details = generate_content(prompt, ollama_url, ollama_model, temperature=0.8)
    details_dict = parse_character_details(details)
    return details_dict

def get_summary(text, db, ollama_url, ollama_model):
    prompt = f"Summarize the following story: {text}"
    summary = generate_content(prompt, ollama_url, ollama_model, temperature=0.8)
    return summary

def process_character_details(names, db, book_details_dict, ollama_url, ollama_model):
    detailed_summaries = {}
    random_names = random.sample(names, min(5, len(names)))
    for i, name in enumerate(random_names, 1):
        logger.info(f"Agent checking character #{i}: {name}")
        summary = generate_character_details(name, ollama_url, ollama_model)
        if "I apologize" not in summary:
            details_dict = parse_character_details(summary)
            logger.info(f"Parsed Character Details: {details_dict}")
            if 'name' in details_dict and details_dict.get('name'):
                save_character_to_db(details_dict, db, book_details_dict)
                detailed_summaries[name] = details_dict
            else:
                logger.info(f"Character name is missing or invalid: {details_dict}")
    return detailed_summaries

def parse_character_details(details):
    details_dict = {}
    current_key = None
    current_value = []

    valid_keys = ["name", "sex", "age", "traits", "behaviors", "background_summary", "dialogue examples"]

    for line in details.split('\n'):
        line = line.strip().replace('**', '')
        if not line:
            continue
        key = line.split(':')[0].strip().lower().replace(' ', '_')
        if ':' in line and key in valid_keys:
            if current_key and current_value:
                details_dict[current_key] = ' '.join(current_value).strip()
            current_key = key
            current_value = [line.split(':', 1)[1].strip()]
        else:
            current_value.append(line.strip())

    if current_key and current_value:
        details_dict[current_key] = ' '.join(current_value).strip()
    return details_dict

def save_character_to_db(details_dict, db_session, book_details_dict):
    logger.debug(f"Saving character to DB: {details_dict}")
    if not db_session.query(Character).filter(Character.name == details_dict['name']).first():
        new_character = Character(
            name=details_dict.get('name'),
            sex=details_dict.get('sex', ''),
            age=details_dict.get('age', ''),
            traits=details_dict.get('traits', ''),
            behaviors=details_dict.get('behaviors', ''),
            background_summary=details_dict.get('background_summary', ''),
            book_title=book_details_dict.get('book_title', ''),
            author=book_details_dict.get('author', ''),
            dialogue_examples=details_dict.get('dialogue_examples', ''),
            genre=book_details_dict.get('genre', '')
        )
        db_session.add(new_character)
        db_session.commit()
        db_session.refresh(new_character)
        logger.debug(f"Character saved: {new_character.id}")
