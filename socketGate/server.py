# -*- coding:utf-8 -*-

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SocketGateServer(Protocol):

    def connectionMade(self):
        print self.transport.getPeer(), u"连接服务器"

    def connectionLost(self, reason):
        print self.transport.getPeer(), u"已断开连接"

    def dataReceived(self, data):
        print data

if __name__ == "__main__":
    factory = Factory()
    factory.protocol = SocketGateServer
    reactor.listenTCP(1234, factory)
    reactor.listenTCP(4321, factory)
    print u"服务器已启动"
    reactor.run()
