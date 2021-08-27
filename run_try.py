from flex_mnist import make_the_network
import networkx as nx


path = "E:/pycharm-program/flex_mnist/network/2021_08_24_19_11_15.gpickle"
network = make_the_network.read_network(path)
print(network.nodes)
for node in network.nodes:
    neighbors = ""
    for i in (nx.neighbors(network, node)):
        neighbors += (str(i) + '  ')
    print(neighbors + '\n')

