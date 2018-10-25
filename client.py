#!/usr/bin/env python
import rpyc
c = rpyc.connect("localhost", 12345)
print c.root.get_ip()
