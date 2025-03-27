# Dockerfile
FROM ubuntu:latest

# Update and install dependencies
RUN apt-get update && apt-get install -y \
    netcat-openbsd \
    fortune-mod \
    cowsay \
    && rm -rf /var/lib/apt/lists/*

# Fix PATH issue for cowsay and fortune
ENV PATH="/usr/games:$PATH"

# Copy the script into the container
COPY wisecow.sh /wisecow.sh

# Make the script executable
RUN chmod +x /wisecow.sh

# Expose the port
EXPOSE 4499

# Set the entry point to the script
ENTRYPOINT ["/wisecow.sh"]

