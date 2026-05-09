# Estágio 1: Build
FROM python:3.11-slim as builder

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Estágio 2: Runtime
FROM python:3.11-slim

WORKDIR /app
# Copia as dependências instaladas do estágio anterior
COPY --from=builder /install /usr/local
COPY . .

EXPOSE 5000

# O comando assume que teremos um factory 'create_app' dentro de src/app.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "src.app:create_app()"]