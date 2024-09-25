#FROM - Image to start from.
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

#RUN - Runs a command in the container. Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 for Flask
EXPOSE 5001

#CMD - Command that should be executed when running the image as a container. Command to run the web app
CMD ["python", "app.py"]
