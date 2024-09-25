<<<<<<< HEAD
# Docker_containers
Test to develop a containerized application and deploy it. The web application shows to the end user an "hello world" landing page along with your name, retrieved from a database.
=======
# Web Application with SQLite

This project contains a simple web server that displays "Hello world, {name}", where `{name}` is retrieved from an SQLite database.

## Project Structure

This project has the following directory structure:

- **database/**: Contains the PostgreSQL database
  - `init.sql`: SQL file that will be executed when the container is started and will contain the creation of the tables and the insertion of data.
  - `Dockerfile`: Dockerfile for the database container

- **webserver/**: Contains the web server application
  - `app.py`: Main web server script
  - `Dockerfile`: Dockerfile for the web server container
  - `requirements.txt`: Python dependencies for the web server

- **docker-compose.yml**: Docker Compose configuration file
- **makefile**: simple Makefile to automate the building and running of the application
- **README.md**: Instructions and documentation for the project


## How to Build and Run

1. Clone this repository:
  ```bash
   git clone <repo-url>
   cd project-root
   ```

2.	Build the containers:
   ```bash
   make build
   ```
  
3.	Run the containers:
   ```bash
   make up
   ```

4.	Show the running containers:
   ```bash
   make ps
   ```

5.	Open a browser and go to http://localhost:5001 to see the message “Hello world, {YourName}”.

6. Stop and remove the containers:
  ```bash
   make down
   ```

>>>>>>> 9b09784 (commit)
