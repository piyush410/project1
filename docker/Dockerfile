# Dockerfile (inside docker/ folder)
FROM python:3.9
WORKDIR /app
# Humein ek step piche ja kar code uthana hoga agar hum docker folder se build kar rahe hain
COPY ../code/ /app/ 
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
