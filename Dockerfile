#############################################
# Stage 1 — Build Stage
#############################################
FROM python:3.11-slim AS builder

WORKDIR /app

# Copy only requirements first to leverage caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all source code
COPY . .

#############################################
# Stage 2 — Runtime Stage
#############################################
FROM python:3.11-slim

WORKDIR /app

# Copy Python installed packages from builder
COPY --from=builder /usr/local/lib/python3.11 /usr/local/lib/python3.11
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy the application code
COPY --from=builder /app /app

# Ensure Python finds your code modules
ENV PYTHONPATH=/app

# Expose FastAPI port
EXPOSE 8000

# Run Uvicorn pointing to your code/app.py
CMD ["uvicorn", "code.app:app", "--host", "0.0.0.0", "--port", "8000"]
