#!/bin/bash
source aws_secrets.txt

docker run --name some-redis -d redis
docker run -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION --link some-redis:redis -it ultrasignupnotifier:test
docker stop some-redis
docker rm some-redis
