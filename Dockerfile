# Use an official Python image from DockerHub
FROM python:3.8-slim

# Set the working directory inside the container
WORKDIR /app

# Install virtualenv
RUN pip install virtualenv

# Set up a virtual environment and activate it
RUN virtualenv venv
ENV PATH="/app/venv/bin:$PATH"

# Copy the requirements file into the container
COPY requirements.txt .

# Install Python dependencies in the virtual environment
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY src/ .

# Specify the command to run on container start
CMD ["python", "./your_script.py"]