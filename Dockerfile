FROM python:3.12-slim

WORKDIR /app

# Copy project files
COPY pyproject.toml ./
COPY app.py ./

# Install dependencies
RUN pip install --no-cache-dir -e .

# Expose port
EXPOSE 8000

# Run the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
