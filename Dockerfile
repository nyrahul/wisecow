FROM python:3.12-slim

# Working directory in the container
WORKDIR /wisecowtest

# Copy the current directory contents into the container at /myapp
COPY . .

# add requirements (to leverage Docker cache)
# ADD ./requirements.txt /usr/src/app/requirements.txt

# install requirements
# RUN pip install -r requirements.txt

# Expose port 3000 for the application
EXPOSE 4499

# Environment variable
ENV NAME Wisecow

# Run app.py when the container launches
CMD ["sh", "wisecow.sh"]