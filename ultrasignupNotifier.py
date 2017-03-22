#!/bin/python
import requests
import logging
import ConfigParser
import redis

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

config = ConfigParser.ConfigParser()
config.read('config.ini')
redis_host = config.get("access", "redis_host")
r = redis.StrictRedis(host=redis_host)

def main(event, context):
    print("do stuff")

def setURL(url):
    print("posting ", url, " to the Redis db")
    r.sadd("ultrasignupNotifier_TEST", url)

def delURL(url):
    print("deleting ", url, " from the Redis db")

def replaceURL(url, url2):
    print("replace ", url, " with ", url2)
