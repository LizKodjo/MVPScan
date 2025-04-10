FROM python:3.12-slim
WORKDIR /app
COPY scanner.py .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 80
CMD ["python", "scanner.py"]