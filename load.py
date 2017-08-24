#!/bin/python

#Can use this example to load data into your test or prod redis
#if doing local test, use the ultrasignupnotifier:test tag, and make sure some-redis is running
#docker run --link some-redis:redis -it ultrasignupnotifier:test load.py
#if doing prod load, use the ultrasignupnotifier:build tag
##source aws_secrets.txt
##docker run -e AWS_ACCESS_KEY_ID -e AWS_SECRET_ACCESS_KEY -e AWS_DEFAULT_REGION -it ultrasignupnotifier:build load.py

from ultrasignupNotifier import *

r.delete(redis_set)
#no business
setURL("https://ultrasignup.com/register.aspx?did=40347", redis_set)
#bfc 2016 -> should redirect to 2017
setURL("https://ultrasignup.com/register.aspx?did=34630", redis_set)
#upchuck
setURL("https://ultrasignup.com/register.aspx?did=43215", redis_set)
#south mountains (opens on Aug 25)
setURL("https://ultrasignup.com/register.aspx?did=49279", redis_set)
