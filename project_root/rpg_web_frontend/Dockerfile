# project_root/rpg_web_frontend/Dockerfile

FROM python:3.9-slim

WORKDIR /usr/src/app

# Copy the requirements file into the container
COPY project_root/rpg_web_frontend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY project_root/rpg_web_frontend ./
COPY project_root/shared ./shared

EXPOSE 5000

# Command to run the application with Gunicorn
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
