FROM python:3.9-alpine

# Set working directory
WORKDIR /app

# Install system dependencies (often needed for pip packages)
RUN apk add --no-cache gcc musl-dev libffi-dev

# Copy requirements first (better layer caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY app.py .

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]