# Use an official PostgreSQL runtime as a parent image
FROM postgres:13

# Add the initialization script
COPY init.sql /docker-entrypoint-initdb.d/
