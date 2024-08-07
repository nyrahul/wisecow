# Use an official Ubuntu as a parent image
FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    netcat \
    fortune-mod \
    cowsay \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY . .

RUN chmod +x wisecow.sh

EXPOSE 4499

CMD ["./wisecow.sh"]
