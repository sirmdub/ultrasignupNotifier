#!/bin/bash

docker build -t ultrasignupnotifier:build .
docker build -t ultrasignupnotifier:deploy . -f Dockerfile.deploy

cd tests
docker build -t ultrasignupnotifier:test .
