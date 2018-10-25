#!/usr/bin/env python
import rpyc
import ConfigParser

def write_information(server, conn):
    file.write(server)
    file.write("{:<30} {:<30}\n".format('The IP:', conn.root.get_ip()))
    file.write("{:<30} {:<30}\n".format('Listening on port:', conn.root.get_port()))
    file.write("\n")

    os_info = conn.root.get_os_information()
    file.write("{:<30} {:<30}\n".format('System name:', os_info[0]))
    file.write("{:<30} {:<30}\n".format('Hostname:', os_info[1]))
    file.write("{:<30} {:<30}\n".format('Release:',os_info[2]))
    file.write("{:<30} {:<30}\n".format('Version:',os_info[3]))
    file.write("{:<30} {:<30}\n".format('Machine type:', os_info[4]))
    file.write("{:<30} {:<30}\n".format('Server UPTime:', conn.root.get_boot_time()))
    file.write("{:<30} {:<30}\n".format('#running proccess:', conn.root.get_proccess_info()))
    file.write("{:<30} {:<3}MB\n".format('Available RAM:', conn.root.get_available_ram()/1024/1024))

def read_config():
    'reading servers configration'
    config = ConfigParser.ConfigParser()
    config.read('config_server.cfg')
    for each_server in config.sections():
        ip =  config.get(each_server, 'ip')
        port =  config.get(each_server, 'port')
        c = rpyc.connect(ip, int(port))
        write_information(each_server, c)

if __name__=="__main__":
    file = open("result.txt","w")
    read_config()
    file.close()
