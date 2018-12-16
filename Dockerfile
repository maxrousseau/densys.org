# python3
FROM python:3.7-slim-stretch

# dependencies needed for package building
RUN apt-get update && apt-get install -y \
	cmake \
	gcc \
	build-essential \
	pkg-config \
	libx11-dev \
	libatlas-base-dev \
	libgtk-3-dev \
	libboost-python-dev

# set working directory to /app
WORKDIR /app

# add the current directory contents into the container at app
ADD . /app

# install the packages that I need through conda
RUN pip install -r requirements.txt

# make port 80 available to the world outside this container
EXPOSE 80

# define environment variable
ENV NAME World

# run my app when the container lauches
CMD ["python", "app.py"]
