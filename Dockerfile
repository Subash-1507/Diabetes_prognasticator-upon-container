# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /usr/src/app
COPY . /app

# Install necessary packages
RUN pip install --no-cache-dir -r requirements.txt

# Uninstall any existing scikit-learn and install the specific version
RUN pip uninstall -y scikit-learn && \
    pip install scikit-learn==1.0.1

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run app.py when the container launches
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
