# Use a base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Make the script executable
RUN chmod +x wisecow.sh

# Expose the port that the app runs on (if applicable)
EXPOSE 4499

# Command to run the application
CMD ["./wisecow.sh"]
