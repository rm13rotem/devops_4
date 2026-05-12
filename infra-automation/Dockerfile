FROM python:3.11-slim

WORKDIR /app

COPY /infra-automation/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["python", "infra-automation/main.py"]
