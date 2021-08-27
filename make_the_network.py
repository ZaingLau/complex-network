import networkx as nx
import random
import pandas as pd
import time
import os
# import matplotlib.pyplot as plt


def choose_the_network(file_time, number, k, p, network_name=["watts"]):
    if not os.path.exists("E:/pycharm-program/flex_mnist/result/" + file_time + "/network/"):
        os.makedirs("E:/pycharm-program/flex_mnist/result/" + file_time + "/network/")
    if network_name == "watts":
        network = nx.watts_strogatz_graph(number, k, p)
    # ADD OTHER NETWORK HERE
    else:
        network = None

    # DEAL IT FOR NOT ILLEGAL
    network = deal_with_single_node(network)

    # SAVE IT   ||   NEED TO BE FIXED
    time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    nx.write_gpickle(network, "E:/pycharm-program/flex_mnist/result/" + file_time + "/network/" + time_now + ".gpickle")
    '''
    degree_list = make_the_degree_list(network)
    df = pd.DataFrame(degree_list)
    df.to_excel("E:/pycharm-program/flex_mnist/network/" + time_now + ".xlsx", header=None, index=False)
    '''

    # ps = nx.circular_layout(network)
    # nx.draw(ws, ps, with_labels = False, node_size = 2)
    # plt.show()

    # print(network.nodes())
    # print(network.degree(1))

    return network


def read_network(path):
    network = nx.read_gpickle(path)
    return network


def deal_with_single_node(network):
    """
    degree_list = make_the_degree_list(network)
    single_index = []
    for i in range(0, len(degree_list)):
        if degree_list[i] == 0:
            single_index.append(i)
    single_list = single_index
    """
    single_list = list(nx.isolates(network))
    for node in single_list:
        nodes_list = (network.nodes()).remove(node)
        network.add_edge(node, random.choice(nodes_list))
    return network


def make_the_degree_list(network):
    nodes_number = nx.classes.number_of_nodes(network)
    degree = []
    for i in range(0, nodes_number):
        degree.append(network.degree(i))
    return degree

