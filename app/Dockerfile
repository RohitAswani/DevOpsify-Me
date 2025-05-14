# Use a base Python image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies (adjust as needed based on your requirements)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file from the host into the container's /app directory
COPY app/requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container's /app directory
COPY app/ /app/

# Expose the port (change if needed for your application)
EXPOSE 5000

# Command to run your app (adjust if needed)
CMD ["python", "main.py"]  # Ensure this is the correct entry point for your app
