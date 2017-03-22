#!/bin/python

from ultrasignupNotifier import *

setURL("http://something", "ultrasignupNotifier_TEST")
#if not r.sismember("", i):

replaceURL("http://something", "http://somethingelse", "ultrasignupNotifier_TEST")
delURL("http://somethingelse", "ultrasignupNotifier_TEST")
