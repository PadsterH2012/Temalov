# Use an official PostgreSQL runtime as a parent image
FROM postgres:13

# Add the initialization script to the image
COPY init.sql /docker-entrypoint-initdb.d/
