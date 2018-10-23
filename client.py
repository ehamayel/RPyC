#!/usr/bin/env python
import rpyc
c = rpyc.connect("localhost", 12345)

print "The ip", c.root.get_ip()
print 'listening on port:', c.root.get_port()
os_info = c.root.get_os_information()
print "System name", os_info[0]
print "hostname", os_info[1]
print "release", os_info[2]
print "version", os_info[3]
print "machine type", os_info[4]
