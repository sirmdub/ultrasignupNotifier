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

def setURL(url, setName):
    print("posting ", url, " to the Redis db")
    r.sadd(setName, url)

def delURL(url, setName):
    print("deleting ", url, " from the Redis db")
    r.srem(setName, url)

def replaceURL(url, url2, setName):
    print("replace ", url, " with ", url2)
    delURL(url,setName)
    setURL(url2,setName)
