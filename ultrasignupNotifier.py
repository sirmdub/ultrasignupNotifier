#!/bin/python
import requests
import logging
import ConfigParser
import redis
import re
import json

logger = logging.getLogger()
logger.setLevel(logging.ERROR)

config = ConfigParser.ConfigParser()
config.read('config.ini')
redis_host = config.get("access", "redis_host")
redis_set = config.get("access", "redis_set")
hipchat_token = config.get("access","hipchat_token")
hipchat_room = config.get("access", "hipchat_room")
r = redis.StrictRedis(host=redis_host)


def main(event, context):
    for url in r.smembers(redis_set):
        print("processing" + url)
        processRace(getPage(url), url)


def processRace(html, url=None):
    if registrationOpen(html):
        processRaceStatus = 'open'
        # if url: hipchat_notify(room=hipchat_room, message=url)
    else:
        processRaceStatus = 'closed'
        if isNextEventAvailable(html):
            nexturl = getRedirectURL('https://ultrasignup.com' + getNextEventURL(html))
            replaceURL(url, nexturl, redis_set)
            processRaceStatus = 'previous'
            print("next event is available, calling processRace on: " + nexturl)
            processRace(getPage(nexturl), nexturl)
    return processRaceStatus

def setURL(url, redis_set):
    print("posting ", url, " to the Redis db", redis_set)
    r.sadd(redis_set, url)

def delURL(url, redis_set):
    print("deleting ", url, " from the Redis db", redis_set)
    r.srem(redis_set, url)

def replaceURL(url, url2, redis_set):
    print("replace ", url, " with ", url2, redis_set)
    delURL(url,redis_set)
    setURL(url2,redis_set)

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
    page = requests.get(url)
    return page.url

def getPage(url):
    page = requests.get(url)
    return page.text

def hipchat_notify(token, room, message, color='yellow', notify=False,
                   format='text', host='api.hipchat.com'):
    """Send notification to a HipChat room via API version 2

    Parameters
    ----------
    token : str
        HipChat API version 2 compatible token (room or user token)
    room: str
        Name or API ID of the room to notify
    message: str
        Message to send to room
    color: str, optional
        Background color for message, defaults to yellow
        Valid values: yellow, green, red, purple, gray, random
    notify: bool, optional
        Whether message should trigger a user notification, defaults to False
    format: str, optional
        Format of message, defaults to text
        Valid values: text, html
    host: str, optional
        Host to connect to, defaults to api.hipchat.com
    """

    if len(message) > 10000:
        raise ValueError('Message too long')
    if format not in ['text', 'html']:
        raise ValueError("Invalid message format '{0}'".format(format))
    if color not in ['yellow', 'green', 'red', 'purple', 'gray', 'random']:
        raise ValueError("Invalid color {0}".format(color))
    if not isinstance(notify, bool):
        raise TypeError("Notify must be boolean")

    url = "https://{0}/v2/room/{1}/share/link".format(host, room)
    headers = {'Content-type': 'application/json'}
    headers['Authorization'] = "Bearer " + token
    payload = {
        'message': '@all',
        'link': message,
        'notify': notify,
        'message_format': format,
        'color': color
    }
    r = requests.post(url, data=json.dumps(payload), headers=headers)
    r.raise_for_status()
