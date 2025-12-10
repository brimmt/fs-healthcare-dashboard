# 1. Base image
FROM python:3.11-slim

# 2. Work directory
WORKDIR /app

# 3. Install system dependencies (needed for PostgreSQL + Supabase libs)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 4. Copy ONLY requirements first for caching
COPY requirements.txt .

# 5. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 6. Now copy the actual code
COPY . .

# 7. Expose port
EXPOSE 8000

# 8. Run FastAPI with Uvicorn in production mode
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]