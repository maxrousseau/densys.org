#!/usr/bin/env bash
# TODO:
# - add time variable for api calls and timeouts

echo "[INFO] local host api call"

curl -s -g -i -H Content-Type:application/json -X POST -d  \
	'{"image":"http://optipng.sourceforge.net/pngtech/img/lena.png",
	"analysis":"asym"}' \
	http://localhost:5000/api/v0.0/jobs/new > local_api_test.log

if grep -q "BAD" local_api_test.log;
then
	echo "[WARNING] local api call error"
	echo "[INFO] view call output in local_api_test.log"
else
	echo "[INFO] local api call completed without error"
fi

echo "[INFO] heroku server api call"

curl -s -g -i -H Content-Type:application/json -X POST -d \
	'{"image":"http://optipng.sourceforge.net/pngtech/img/lena.png",
	"analysis":"asym"}' \
	https://stormy-hollows-38428.herokuapp.com/api/v0.0/jobs/new \
	> server_api_test.log

if grep -q "BAD" server_api_test.log;
then
	echo "[WARNING] heroku server api call error"
	echo "[INFO] view call output in server_api_test.log"
else
	echo "[INFO] heroku server api call completed without error"
fi
