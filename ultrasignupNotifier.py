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
    #do stuff

def setURL(url):
    #post an URL to the Redis db
