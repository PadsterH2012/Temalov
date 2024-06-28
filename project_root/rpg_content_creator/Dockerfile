FROM python:3.9-slim

WORKDIR /usr/src/app

COPY project_root/rpg_content_creator/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY project_root/rpg_content_creator ./
COPY project_root/shared ./shared

EXPOSE 5000

CMD ["python", "app.py"]
