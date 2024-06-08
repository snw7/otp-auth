# Use slim Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .
COPY app.py .
COPY .env .

VOLUME /etc/letsencrypt/

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt; mkdir logs

# Open port to the world
EXPOSE <your-port>

# Run the application
CMD [ "python", "app.py" ]