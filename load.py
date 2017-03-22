#!/bin/python

#Can use this example to load data into your test or prod redis
#if doing local test, use the ultrasignupnotifier:test tag, and make sure some-redis is running
#docker run --link some-redis:redis -it ultrasignupnotifier:test load.py
#if doing prod load, use the ultrasignupnotifier:build tag
#docker run -it --entrypoint sh ultrasignupnotifier:build load.py

from ultrasignupNotifier import *

setURL("https://ultrasignup.com/register.aspx?did=40347")
setURL("https://ultrasignup.com/register.aspx?did=34630")
setURL("https://ultrasignup.com/register.aspx?did=43215")
setURL("https://ultrasignup.com/register.aspx?did=44227")
