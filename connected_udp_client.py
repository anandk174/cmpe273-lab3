from __future__ import print_function
from twisted.internet.protocol import DatagramProtocol
from twisted.internet import reactor

class Helloer(DatagramProtocol):

    def startProtocol(self):
        host = "127.0.0.1"
        port = 8000

        self.transport.connect(host, port)
        client_name = input("Please enter your name:")
        self.transport.write(str.encode(client_name))

    def datagramReceived(self, data, addr):
        str_data = str(data)
        print("server says: {} \n from {}".format(str_data, addr))

    def connectionRefused(self):
        print("Nobody is listening")

reactor.listenUDP(8001, Helloer())
reactor.run()   

