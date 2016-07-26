from twisted.internet import reactor
from twisted.web.client import downloadPage
import sys

def printError(failure):
    print(failure, file=sys.stderr)

def stop(result):
    reactor.stop()

if len(sys.argv) != 3:
    print("Usage: python download_resource.py <URL> <output file>", file=sys.stderr)
    exit(1)

d = downloadPage(sys.argv[1], sys.argv[2])
d.addErrback(printError)
d.addBoth(stop)

reactor.run()

