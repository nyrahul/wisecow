# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN apt-get update && \
    apt-get install -y fortune-mod cowsay && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Make port 4499 available to the world outside this container
EXPOSE 4499

# Run wisecow.sh when the container launches
CMD ["./wisecow.sh"]
