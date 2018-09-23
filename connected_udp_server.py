from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class HelloerServer(DatagramProtocol):
    def startProtocol(self):
        host = "127.0.0.1"
        port = 8001
        self.transport.connect(host, port)
        


    def datagramReceived(self, data, addr):        
        self.transport.write(b"hi " + data)

reactor.listenUDP(8000, HelloerServer())
reactor.run()
