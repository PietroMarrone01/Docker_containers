# Use the official PostgreSQL image as a base
FROM postgres:14

# Create a folder to copy the initialization scripts
RUN mkdir -p /docker-entrypoint-initdb.d

# Copy the SQL schema that creates the tables and populates the database
COPY init.sql /docker-entrypoint-initdb.d/

# Expose the default PostgreSQL port
EXPOSE 5432




