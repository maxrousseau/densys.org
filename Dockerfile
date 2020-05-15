# python3
FROM python:3.7-slim-stretch

# dependencies needed for package building
RUN apt-get update && apt-get install -y \
	gcc \
	build-essential \
	pkg-config \

# set working directory to /app
WORKDIR /app

# add the current directory contents into the
# container at app
ADD . /app

# install the packages that I need through
# conda
RUN pip install -r requirements.txt

# make port 80 available to the world outside
# this container
EXPOSE 80

# define environment variable
ENV NAME World
