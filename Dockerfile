FROM python:3.9-alpine

# Update the OS
RUN apk update && \
    apk upgrade

# Set the working directory
WORKDIR /src/app

# Install requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the project files
COPY ./ ./

# Do the migrations
RUN python manage.py migrate

# Start the app
CMD python manage.py runserver 0.0.0.0:8000

# Expose the app port
EXPOSE 8000