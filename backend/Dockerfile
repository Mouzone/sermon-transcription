# Use an official Python runtime as a parent image
FROM python:3.12-slim

RUN pip install --no-cache-dir uv

# Set the working directory in the container
WORKDIR /app

# Copy dependency files first (for caching)
COPY pyproject.toml uv.lock ./

# Install dependencies using UV
RUN uv pip install --no-cache-dir -r uv.lock

# Copy the rest of the application
COPY . .

# Expose the port your app runs on
EXPOSE 8000

# Run the application
CMD ["python", "main.py"]