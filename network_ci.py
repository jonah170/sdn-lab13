import sys

from mininet.net import Mininet
from mininet.node import OVSBridge
from mininet.topo import Topo
from mininet.log import setLogLevel


class LabTopology(Topo):

    def build(self):

        s1 = self.addSwitch("s1")

        h1 = self.addHost("h1")
        h2 = self.addHost("h2")
        h3 = self.addHost("h3")

        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)


def main():

    topology = LabTopology()

    net = Mininet(
        topo=topology,
        switch=OVSBridge,
        controller=None,
        autoSetMacs=True
    )

    try:

        net.start()

        print("\nTesting network connectivity...\n")

        packet_loss = net.pingAll()

        print(
            f"\nObserved packet loss: "
            f"{packet_loss}%"
        )

        if packet_loss != 0:

            print("NETWORK TEST FAILED")
            return 1

        print("NETWORK TEST PASSED")
        return 0

    finally:

        net.stop()


if __name__ == "__main__":

    setLogLevel("info")
    sys.exit(main())