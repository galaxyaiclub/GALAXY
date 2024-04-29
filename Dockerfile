FROM python:3.10-slim-buster

WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt requirements.txt
RUN python -m venv venv && \
    /app/venv/bin/pip install --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Adjust permissions for translations directory (replace with appropriate permissions)
RUN chmod -R 755 translations

# Set container user (optional)
# USER appuser

# Specify command to run the application
CMD ["python3", "./run.py"]
