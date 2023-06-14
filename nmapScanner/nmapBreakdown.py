#u2041563 Python nmap parser

import nmap
import socket

class netScan:
    #Defining variable contents if they are not added by the user
    def __init__(self, ipAddr, protocol, portNum=None, arguments='-sV', timeout=0):
        self.ipAddr = ipAddr
        self.portNum = portNum
        self.arguments = arguments
        self.timeout = timeout
        self.protocol = protocol

    #Get list of all hosts on a network
    def getHosts(self):
        nm = nmap.PortScanner()
        self.arguments = '-sn'
        netHosts = nm.scan(hosts=str(self.ipAddr), arguments=self.arguments)
        hostList = nm.all_hosts()
        for i in range(len(hostList)):
            hostElement = str(hostList[i])
            print('IP:', hostList[i], 'Hostname:', nm[hostList[i]].hostname())

    #Get running protocols from a host on the network
    def getProtocol(self):
        nm = nmap.PortScanner()
        netProtocols = nm.scan(hosts=str(self.ipAddr))
        hostList = nm.all_hosts()
        for i in range(len(hostList)):
            print('Protocols used by:', hostList[i], 'Protocol:', nm[hostList[i]].all_protocols())

    #get network status
    def isUp(self):
        nm = nmap.PortScanner()
        netisUp = nm.scan(hosts=str(self.ipAddr))
        hostList = nm.all_hosts()
        for i in range(len(hostList)):
            print('Status of', hostList[i], ':', nm[hostList[i]].state())

    #get open ports
    def getOpenPorts(self):
        nm = nmap.PortScanner()
        netOpenPorts = nm.scan(hosts=str(self.ipAddr))
        hostList = nm.all_hosts()
        for i in range(len(hostList)):
            print('Open ports on protocol', self.protocol, 'for IP Address', hostList[i], nm[hostList[i]][self.protocol].keys())
    
    #get more information about an open port
    def morePortInfo(self):
        nm = nmap.PortScanner()
        netPortInfo = nm.scan(hosts=str(self.ipAddr))
        hostList = nm.all_hosts()
        for i in range(len(hostList)):
            print('More info on port', self.portNum, 'for IP Address', hostList[i], nm[hostList[i]][self.protocol][self.portNum])

###Additional Implementation###
class socketScan:
    #Subsystem 1
    def scanSock(self):
        print('Performing socket scan')

class nmapScan:
    #Subsystem 2
    def scanNmap(self):
        print('Performing nmap scan')

class scanner:
    #Facade
    def __init__(self):
        self.socketscanner = socketScan()
        self.nmapscanner = nmapScan()

    def startScanning(self):
        self.socketscanner.scanSock()
        self.nmapscanner.scanNmap()

if __name__ == "__main__":
    scanner = scanner()
    scanner.startScanning()
###End of additional implementation###
        
def main():
    print('Set network scan parameters')
    ipAddr = input('IP Address or Domain Name:')
    #Checking for domain name to resolve
    if ipAddr[0].isalpha():
        ipAddr = socket.gethostbyname(ipAddr)
    portNum = input('Port:')
    #checking for missing portNum data
    if not portNum:
        portNum = None
    else:
        portNum = int(portNum)
    timeout = input('Timeout:')
    #checking for missing portNum data
    if not timeout:
        timeout = 0
    else:
        timeout = int(timeout)
    protocol = input('Protocol:')
    #checking for missing protocol
    if not protocol:
        protocol = None
        
    clientScan = netScan(ipAddr, protocol, portNum, timeout)
    
    print('\n\nSelect a service(s)')
    print('\nGet hosts (1)\nGet Protocol (2)\nCheck Status (3)\nCheck Open Ports (4)\nMore Open Port Info (5)')
    service = input(":")
    if '1' in service:
        print('Getting hosts')
        clientScan.getHosts()
    if '2' in service:
        print('Getting protocol')
        clientScan.getProtocol()
    if '3' in service:
        print('Getting status')
        clientScan.isUp()
    if '4' in service:
        print('Checking Open Ports')
        clientScan.getOpenPorts()
    if '5' in service:
        print('Getting More Port Info')
        clientScan.morePortInfo()

main()
