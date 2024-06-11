cat Dockerfile
FROM alpine:latest
RUN apk add --no-cache bash
# Install dependencies and build tools
RUN apk update && \
    apk add --no-cache fortune netcat-openbsd perl perl-utils

# Download and build cowsay from source
RUN wget -O- https://github.com/tnalpgge/rank-amateur-cowsay/archive/master.tar.gz | tar zx && \
    cd rank-amateur-cowsay-master && \
    ./install.sh /usr/local

# Create a working directory
WORKDIR /usr/src/app

# Copy the script and response file (assuming wisecow.sh and response are in the same directory as the Dockerfile)
COPY wisecow.sh .

# Make the script executable
RUN chmod +x wisecow.sh

# Expose the port the app runs on
EXPOSE 4499

# Run the script
CMD ["./wisecow.sh"]
