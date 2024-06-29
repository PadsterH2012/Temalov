import PyPDF2

def extract_characters(file):
    # Implement your character extraction logic here
    reader = PyPDF2.PdfFileReader(file)
    characters = []
    for page in range(reader.numPages):
        text = reader.getPage(page).extractText()
        # Process text to extract characters
        # For demonstration purposes, let's assume characters are extracted
        characters.append({"page": page, "content": text})
    return characters

def extract_quests(file):
    # Implement your quest extraction logic here
    reader = PyPDF2.PdfFileReader(file)
    quests = []
    for page in range(reader.numPages):
        text = reader.getPage(page).extractText()
        # Process text to extract quests
        # For demonstration purposes, let's assume quests are extracted
        quests.append({"page": page, "content": text})
    return quests
