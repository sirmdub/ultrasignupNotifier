#!/bin/python

from ultrasignupNotifier import *

setName = "ultrasignupNotifier_TEST"

setURL("http://something", setName)
if not r.sismember(setName, "http://something"):
    raise Exception("FAILED: setURL did not set URL in db")

replaceURL("http://something", "http://somethingelse", setName)
if r.sismember(setName, "http://something"):
    raise Exception("FAILED: replaceURL did not remove original URL from db")
if not r.sismember(setName, "http://somethingelse"):
    raise Exception("FAILED: replaceURL did not set new URL in db")

delURL("http://somethingelse", setName)
if r.sismember(setName, "http://somethingelse"):
    raise Exception("FAILED: delURL did not remove URL from db")
