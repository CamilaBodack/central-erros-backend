# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.6

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /centralerrors_service

# Set the working directory to /centralerrors_service
WORKDIR /centralerrors_service

# Copy the current directory contents into the container at /centralerrors_service
ADD . /centralerrors_service/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
