# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install system dependencies for tkinter
RUN apt-get update && apt-get install -y tk && rm -rf /var/lib/apt/lists/*

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY app.py .

# Define environment variable for tkinter to connect to the host's X server
ENV DISPLAY :0

# Run app.py when the container launches
CMD ["python", "app.py"] 