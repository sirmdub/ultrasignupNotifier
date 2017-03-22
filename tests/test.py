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

if not registrationOpen("<html><itsOPEN>Registration closes</itsOPEN></html>"):
    raise Exception("FAILED: registrationOpen thinks an open race is not open for registration")

if registrationOpen("<html><itsNOT>Registration Opens</itsNOT></html>"):
    raise Exception("FAILED: registrationOpen thinks a closed race is open for registration")

#test registrationOpen on html files (open, closed, previous, soldout)

#previous test cases
#identify its a previous race
#url gets replaced in db, when its identified as a previous race
#new url gets tested after its identified and replaced
