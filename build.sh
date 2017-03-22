#!/bin/bash

docker build -t ultrasignupnotifier:build .
docker create --name ultrasignupnotifierBuild ultrasignupnotifier:build
docker cp ultrasignupnotifierBuild:/usr/src/app/ultrasignupNotifier.zip /tmp/
docker rm ultrasignupnotifierBuild
