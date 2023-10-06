# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Flask
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0

# Create and set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the application runs on
EXPOSE 5000

# Run app.py when the container launches
CMD ["gunicorn", "-k", "gevent", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]

