# ---------- Stage 1: Build dependencies ----------
FROM python:3.9-alpine AS builder

WORKDIR /app

# Install build dependencies
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY requirements.txt .

# Install dependencies into a folder
RUN pip install --no-cache-dir --prefix=/install -r requirements.txt


# ---------- Stage 2: Final image ----------
FROM python:3.9-alpine

WORKDIR /app

# Copy installed dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY ./app/app.py .

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app.py"]