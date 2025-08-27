# Dockerfile
FROM python:3.12-slim

# Устанавливаем зависимости
WORKDIR /app

COPY requirements/base-requirements.txt .
COPY requirements/prod-requirements.txt .

RUN pip install --no-cache-dir -r prod-requirements.txt

# Копируем код
COPY . .

# Запускаем
CMD ["python", "main.py"]
