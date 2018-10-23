#!/usr/bin/env python
import rpyc
c = rpyc.connect("localhost", 12345)
print "{:<30} {:<30}".format('The IP:', c.root.get_ip())
print "{:<30} {:<30}".format('Listening on port:', c.root.get_port())
os_info = c.root.get_os_information()
print "{:<30} {:<30}".format('System name:', os_info[0])
print "{:<30} {:<30}".format('Hostname:', os_info[1])
print "{:<30} {:<30}".format('Release:',os_info[2])
print "{:<30} {:<30}".format('Version:',os_info[3])
print "{:<30} {:<30}".format('Machine type:', os_info[4])

