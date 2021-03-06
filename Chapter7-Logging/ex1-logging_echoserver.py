from twisted.internet import protocol, reactor
from twisted.python import log
import sys

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        log.msg(data)
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

# log.startLogging(open('echo.log', 'w'))
log.startLogging(sys.stdout)
reactor.listenTCP(8000, EchoFactory())
reactor.run()
