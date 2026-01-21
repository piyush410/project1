# Python ka official image use karein
FROM python:3.9-slim

# Work directory set karein
WORKDIR /app

# Requirements copy karke install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Saara code copy karein
COPY . .

# Flask port 5000 expose karein
EXPOSE 5000

# App chalane ki command
CMD ["python", "app.py"]
