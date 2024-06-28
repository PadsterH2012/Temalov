FROM python:3.9-slim

WORKDIR /usr/src/app

COPY project_root/rpg_web_frontend/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY project_root/rpg_web_frontend/ ./
COPY project_root/shared ./shared
COPY project_root/tests ./tests

EXPOSE 5000

CMD ["python", "app.py"]
