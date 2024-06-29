FROM python:3.9-slim

WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY project_root/rpg_content_creator/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code and shared directory
COPY project_root/rpg_content_creator ./
COPY project_root/shared ./shared

EXPOSE 8001

# Command to run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8001", "run:app"]