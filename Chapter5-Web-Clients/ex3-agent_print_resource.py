import sys

from twisted.internet import reactor
from twisted.internet.defer import Deferred
from twisted.internet.protocol import Protocol
from twisted.web.client import Agent

class ResourcePrinter(Protocol):
    def __init__(self, finished):
        self.finished = finished

    def dataReceived(self, data):
        print(data)

    def connectionLost(self, reason):
        self.finished.callback(None)

def printResource(response):
    finished = Deferred()
    response.deliverBody(ResourcePrinter(finished))
    return finished

def printError(failure):
    print(failure, file=sys.stderr)

def stop(result):
    reactor.stop()

if len(sys.argv) != 2:
    print("Usage: python agent_print_resource.py URL", file=sys.stderr)
    exit(1)

agent = Agent(reactor)
d = agent.request('GET', sys.argv[1])
d.addCallbacks(printResource, printError)
d.addBoth(stop)

reactor.run()
