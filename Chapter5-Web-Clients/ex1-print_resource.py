from twisted.internet import reactor
from twisted.web.client import getPage
import sys

def printPage(result):
    print(result)

def printError(failure):
    print(failure, file=sys.stderr)

def stop(result):
    reactor.stop()

if len(sys.argv) != 2:
    print("Usage: python print_resource.py <URL>", file=sys.stderr)
    exit(1)

d = getPage(sys.argv[1])
d.addCallbacks(printPage, printError)
d.addBoth(stop)

reactor.run()
