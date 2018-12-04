#!/usr/bin/python 
from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import OVSController
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.log import setLogLevel
from mininet.cli import CLI


'''
Single switch connected to n hosts.
'''
class SingleSwitchTopo(Topo):
    def build(self, n = 2):
        # Add a switch to a topology
        switch = []  #store all switches
        for i in range(5):
            s = self.addSwitch('switch' + str(i+1) ) 
            switch.append(s)
        # Add the host and link to a topology
        host = []
        for i in range(10):   #same as above
            # Add a host to a topology
            h = self.addHost('host' + str(i+1))
            host.append(h)

        # Add a bidirectional link one by one
        self.addLink(host[1-1], switch[2-1], bw = 14, delay = '5ms', loss = 13)
        self.addLink(host[2-1], switch[2-1], bw = 12, delay = '4ms', loss = 15)
        self.addLink(switch[1-1], switch[2-1], bw = 30, delay = '0.087ms', loss = 3)
        self.addLink(host[5-1], switch[1-1], bw = 22, delay = '3ms', loss = 9)
        self.addLink(switch[1-1], switch[4-1], bw = 38, delay = '0.076ms', loss = 4)
        self.addLink(host[9-1], switch[4-1], bw = 30, delay = '7ms', loss = 12)
        self.addLink(host[7-1], switch[1-1], bw = 18, delay = '4ms', loss = 6)
        self.addLink(switch[1-1], switch[3-1], bw = 35, delay = '0.048ms', loss = 2)
        self.addLink(host[3-1], switch[3-1], bw = 15, delay = '3ms', loss = 8)
        self.addLink(host[4-1], switch[3-1], bw = 11, delay = '2ms', loss = 9)
        self.addLink(host[8-1], switch[1-1], bw = 20, delay = '2ms', loss = 8)
        self.addLink(switch[1-1], switch[5-1], bw = 40, delay = '0.052ms', loss = 2)
        self.addLink(host[10-1], switch[1-1], bw = 25, delay = '5ms', loss = 1)
        self.addLink(host[6-1], switch[1-1], bw = 25, delay = '1ms', loss = 7)

'''
Create and test a simple network
'''
def simpleTest():
    # Create a topology with 2 hosts and 1 switch
    topo = SingleSwitchTopo(n = 2)
    # Create and manage a network with a OvS controller and use TCLink
    net = Mininet(
        topo = topo, 
        controller = OVSController,
        link = TCLink)
    # Start a network
    net.start()
    # Test connectivity by trying to have all nodes ping each other
    print("Testing network connectivity")
    net.pingAll()
    dumpNodeConnections(net.hosts)
    dumpNodeConnections(net.switches)
    # enter CLI mode instead of stop the network
    CLI(net)

'''
Main (entry point)
'''
if __name__ == '__main__':
    # Tell mininet to print useful information
    setLogLevel('info')
    # Create and test a simple network
simpleTest()
