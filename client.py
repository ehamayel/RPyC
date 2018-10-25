#!/usr/bin/env python
import rpyc
import ConfigParser

#reading servers configration
config = ConfigParser.ConfigParser()
config.read('config_server.cfg')
for each_server in config.sections():
    ip =  config.get(each_server, 'ip')
    port =  config.get(each_server, 'port')
    c = rpyc.connect(ip, port)

file = open("result.txt", "w")
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
