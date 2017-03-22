#!/bin/python
import requests
import logging
import ConfigParser
import redis
import re

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

def registrationOpen(html):
    return True if "Registration closes" in html else False

def isNextEventAvailable(html):
    searchObj = re.search( r'See the \d{4} event', html, re.I)
    return True if searchObj else False

def getNextEventURL(html):
    #I'm sure lxml and xpath is the way to go... tried xpath for too long, when a simple regex gets it done
    searchObj = re.search( r'ContentPlaceHolder1_hlCurrentEventPage" class="errormessage" href="/register.aspx\?eid=\d+"', html)
    if searchObj:
        searchObj2 = re.search(r'/register.aspx\?eid=\d+', searchObj.group())
        return searchObj2.group()
    else:
        return "i got nothing"

def getRedirectURL(url):
    return "i got nothing"
