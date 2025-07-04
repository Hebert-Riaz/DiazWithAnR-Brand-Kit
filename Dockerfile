# Use official Python base image
FROM python:3.11-slim

# Set working directory in the container
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the rest of your code
COPY . .

# Default command
CMD ["python", "main.py"]
# Expose the port the app runs on
EXPOSE 8000



