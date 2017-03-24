#!/bin/python
from ultrasignupNotifier import *

def fileToString(fileName):
    f = open(fileName, 'r')
    returnString = f.read()
    f.close()
    return returnString


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
if registrationOpen(fileToString('tests/open.html')):
    print("registrationOpen True on open.html")
else:
    raise Exception("FAILED: registrationOpen on open.html thinks an open race is not open for registration")

if not registrationOpen(fileToString('tests/closed.html')):
    print("registrationOpen False on closed.html")
else:
    raise Exception("FAILED: registrationOpen on closed.html thinks a closed race is open for registration")

if not registrationOpen(fileToString('tests/previous.html')):
    print("registrationOpen False on previous.html")
else:
    raise Exception("FAILED: registrationOpen on previous.html thinks a closed race is open for registration")

#identify its a previous race
if isNextEventAvailable(fileToString('tests/previous.html')):
    print("isNextEventAvailable True on previous.html")
else:
    raise Exception("FAILED: isNextEventAvailable on previous.html does not identify correctly")

if not isNextEventAvailable(fileToString('tests/open.html')):
    print("isNextEventAvailable False on open.html")
else:
    raise Exception("FAILED: isNextEventAvailable on open.html does not identify correctly")

if not isNextEventAvailable(fileToString('tests/closed.html')):
    print("isNextEventAvailable False on closed.html")
else:
    raise Exception("FAILED: isNextEventAvailable on closed.html does not identify correctly")


testgetNextEventURL = getNextEventURL(fileToString('tests/previous.html'))
if testgetNextEventURL == "/register.aspx?eid=4327":
    print("getNextEventURL on previous.html PASS")
else:
    print("getNextEventURL returned: ", testgetNextEventURL)
    raise Exception("FAILED: getNextEventURL on previous.html does not find '/register.aspx?eid=4327'")

testgetNextEventURL = getNextEventURL(fileToString('tests/closed.html'))
if testgetNextEventURL == "i got nothing":
    print("getNextEventURL on closed.html PASS")
else:
    print("getNextEventURL returned: ", testgetNextEventURL)
    raise Exception("FAILED: getNextEventURL on closed.html found something, but shouldn't have")


testgetRedirectURL = getRedirectURL('http://ultrasignup.com/register.aspx?eid=4327')
if testgetRedirectURL == "http://ultrasignup.com/register.aspx?did=41232":
    print("getRedirectURL http PASS")
else:
    print("getRedirectURL returned: ", testgetRedirectURL)
    raise Exception("FAILED: getRedirectURL on 'http://ultrasignup.com/register.aspx?eid=4327' does not find 'http://ultrasignup.com/register.aspx?did=41232'")

testgetRedirectURL = getRedirectURL('https://ultrasignup.com/register.aspx?eid=4327')
if testgetRedirectURL == "https://ultrasignup.com/register.aspx?did=41232":
    print("getRedirectURL https PASS")
else:
    print("getRedirectURL returned: ", testgetRedirectURL)
    raise Exception("FAILED: getRedirectURL on 'https://ultrasignup.com/register.aspx?eid=4327' does not find 'https://ultrasignup.com/register.aspx?did=41232'")


testprocessRace = processRace(fileToString('tests/open.html'))
if testprocessRace == 'open':
    print("testprocessRace on open.html PASS")
else:
    print("processRace returned: ", testprocessRace)
    raise Exception("FAILED: processRace on open.html did not return open")

testprocessRace = processRace(fileToString('tests/closed.html'))
if testprocessRace == 'closed':
    print("testprocessRace on closed.html PASS")
else:
    print("processRace returned: ", testprocessRace)
    raise Exception("FAILED: processRace on closed.html did not return closed")

testprocessRace = processRace(fileToString('tests/previous.html'), setName=setName)
if testprocessRace == 'previous':
    print("testprocessRace on previous.html PASS")
else:
    print("processRace returned: ", testprocessRace)
    raise Exception("FAILED: processRace on previous.html did not return previous")

#url gets replaced in db, when its identified as a previous race
if r.sismember(setName, "https://ultrasignup.com/register.aspx?did=41232"):
    print("processRace on previous.html replaces URL in db PASS")
else:
    raise Exception("FAILED: processRace on previous.html did not set new URL in db")

#test that notification is called?
#new url gets tested after its identified and replaced

###############ALL UNIT TESTS PASS###############
###############FUNCTIONALLY TEST MAIN NOW###############
setName = "ultrasignupNotifier_FUNCTIONAL"
setURL("https://ultrasignup.com/register.aspx?did=40347", setName)
setURL("https://ultrasignup.com/register.aspx?did=34630", setName)
setURL("https://ultrasignup.com/register.aspx?did=43215", setName)
setURL("https://ultrasignup.com/register.aspx?did=44227", setName)

main(None, None, setName)
