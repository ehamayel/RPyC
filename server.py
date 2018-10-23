#!/usr/bin/env python
import rpyc
import socket
import os
import platform
import multiprocessing
class MyService(rpyc.Service):
    def on_connect(self, conn):
        print "A client connected to the server" 
        pass

    def on_disconnect(self, conn):
        print "A client diss connected from the server"
        pass

    def exposed_get_ip(self):
        ip = socket.gethostbyname(socket.gethostname())
        return ip

    def exposed_get_port(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 0))
        port_num =  sock.getsockname()[1]
        return port_num

    def exposed_get_os_information(self):
        #return platform.uname()
        print os.uname()[0]
        return os.uname() #object with five attributes:
                          #sysname - operating system name
                          #nodename - name of machine on network
                          #release - operating system release
                          #version - operating system version
                          #machine - hardware identifier

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=12345)
    t.start()
