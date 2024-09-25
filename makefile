# Build the web and database containers
build:
	docker compose build

# Run the containers
up:
	docker compose up --build

# Stop and remove containers
down:
	docker compose down

# Show the running containers
ps:
	docker compose ps

