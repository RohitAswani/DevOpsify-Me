FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the requirements.txt file to /app in the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "main.py"]
