#!/usr/bin/env python
import rpyc
c = rpyc.connect("localhost", 12345)
file = open("config.xml", "w")

file.write("[server1]\n")
file.write("{:<30} {:<30}\n".format('The IP:', c.root.get_ip()))
file.write("{:<30} {:<30}\n".format('Listening on port:', c.root.get_port()))
file.write("\n")

os_info = c.root.get_os_information()
file.write("{:<30} {:<30}\n".format('System name:', os_info[0]))
file.write("{:<30} {:<30}\n".format('Hostname:', os_info[1]))
file.write("{:<30} {:<30}\n".format('Release:',os_info[2]))
file.write("{:<30} {:<30}\n".format('Version:',os_info[3]))
file.write("{:<30} {:<30}\n".format('Machine type:', os_info[4]))
file.write("{:<30} {:<30}\n".format('Server UPTime:', c.root.get_boot_time()))
file.write("{:<30} {:<30}\n".format('#running proccess:', c.root.get_proccess_info()))
file.write("{:<30} {:<3}MB\n".format('Available RAM:', c.root.get_available_ram()/1024/1024))
file.close()
