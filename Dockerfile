# Use official Python base image
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt (if you have one) and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy entire project code into the container
COPY . .

# Command to run your pipeline or entry script
CMD  ["dvc", "repro"]
