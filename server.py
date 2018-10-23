#!/usr/bin/env python
import rpyc
import socket
import os
import platform
import multiprocessing
import psutil
import datetime
class MyService(rpyc.Service):
    def on_connect(self, conn):
        print "A client connected to the server" 
        pass

    def on_disconnect(self, conn):
        print "A client diss connected from the server"
        pass

    def get_ip(self):
        ip = socket.gethostbyname(socket.gethostname())
        return ip

    def get_port(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind(('0.0.0.0', 0))
        port_num =  sock.getsockname()[1]
        return port_num

    def get_os_information(self):
        #return platform.uname()
        return os.uname() #object with five attributes:
                          #sysname - operating system name
                          #nodename - name of machine on network
                          #release - operating system release
                          #version - operating system version
                          #machine - hardware identifier

    def get_boot_time(self):
        #return server uptime in 'YYYY-MM-DD HH:MM:SS'
        return datetime.datetime.fromtimestamp(
               psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")

    def get_proccess_info(self):
        return psutil.cpu_count()

    def get_available_ram(self):
        return psutil.virtual_memory().active
        

if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(MyService, port=12345,
                       protocol_config={'allow_public_attrs': True})
    t.start()
