#!/usr/bin/env bash
# TODO:
# - add time variable for api calls and timeouts

echo "[INFO] local host api call"

curl -s -g -i -H Content-Type:application/json -X POST -d  \
	'{"image":"http://optipng.sourceforge.net/pngtech/img/lena.png",
	"analysis":"asym"}' \
	http://localhost:5000/api/v0.0/jobs/new > log/local_api_test.log

if [ $? -eq 0 ];
then
	echo "[INFO] local api call completed without error"
else
	echo "[WARNING] local api call error"
	echo "[INFO] view call output in local_api_test.log"
fi

echo "[INFO] heroku server api call"

curl -s -g -i -H Content-Type:application/json -X POST -d \
	'{"image":"http://optipng.sourceforge.net/pngtech/img/lena.png",
	"analysis":"asym"}' \
	https://stormy-hollows-38428.herokuapp.com/api/v0.0/jobs/new \
	> log/server_api_test.log

if [ $? -eq 0 ];
then
	echo "[INFO] heroku server api call completed without error"
else
	echo "[WARNING] heroku server api call error"
	echo "[INFO] view call output in server_api_test.log"
fi
