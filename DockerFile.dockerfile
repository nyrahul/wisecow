# Use a Node.js base image
FROM node:14

# Set working directory
WORKDIR /usr/src/app

# Copy package.json and package-lock.json to work directory
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the application code
COPY . .

# Expose port 3000
EXPOSE 3000

# Command to run the application
CMD ["node", "app.js"]
