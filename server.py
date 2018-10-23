#!/usr/bin/env python
import rpyc
class MyService(rpyc.Service):
    def on_connect(self, conn):
        print "A client connected to the server" 
        pass
    def on_disconnect(self, conn):
        print "A client diss connected from the server"
        pass
    def exposed_get_ip(self):
        import socket
        ip=socket.gethostbyname(socket.gethostname())
        print ip
        return ip

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=12345)
    t.start()
