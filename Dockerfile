# Use the official Python base image
FROM python:3.9-slim

# Set environment variables
# Ensures Python output is sent straight to the terminal without buffering
ENV PYTHONUNBUFFERED 1

# Create a working directory for the app
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt /app/

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Expose the port the app runs on
EXPOSE 8080

# Command to run the Flask application using Werkzeug
CMD ["python", "app.py"]
