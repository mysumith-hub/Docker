touch Dockerfile

Add the following content to Dockerfile
--------------------------------------------------------------------------------
# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install Flask

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME Flask-world

# Run app.py when the container launches
CMD ["python","api.py"]
--------------------------------------------------------------------------------
- To create image
docker build -t <name>:<tag_version> .
docker build -t flask-api:1.0.0 .

$ docker images
REPOSITORY                                      TAG                 IMAGE ID            CREATED             SIZE
flask-api                                       latest              6414d3afd432        7 minutes ago       699MB

docker run -d -p 8888:80 flask-api

--------------------------------------------------------------------------------
Pushing docker images to our own registry

We can create our own registry by
-- docker pull registry
-- docker run -d -p 5000:5000 --name localregistry registry

1. First tag the image with version/latest:
docker tag flask-api:latest localhost:5000/flask-api:1.0.0
2. Push the image
docker push localhost:5000/flask-api:1.0.0

we can use below api to check the images in regostry
http://localhost:5000/v2/_catalog
Ex Response:
{
  "repositories": [
    "flask-api",
    "jenkins"
  ]
}

We can also see the list versions taged in regitry for particular project
http://localhost:5000/v2/flask-api:1.0.0/tags/list
