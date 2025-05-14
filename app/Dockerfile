# Use a base Python image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install system dependencies (add more as needed)
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements.txt file to /app in the container
COPY requirements.txt /app/requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . /app

# Run the app (or start your app as per your need)
CMD ["python", "app.py"]  # Change this as per your app
