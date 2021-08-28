from flex_mnist import read_the_image as rdimg
from flex_mnist import mark_the_image as mark
from flex_mnist import make_the_network as get_net

import random
import time

time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())

# params
nodes_number = 784
k = random.randint(2, nodes_number)
p = 0.2

# PATHs
train_img_path = 'E:/cifar-10-python/cifar-10-batches-py/data_batch_'
test_img_path = 'E:/cifar-10-python/cifar-10-batches-py/test_batch'

# get train and test set, as dictionary
train_dic = {}
for i in range(1,6):
    tr_data_list, tr_labels_list = rdimg.load_image(train_img_path + str(i))
    d = rdimg.make_the_class_dic(tr_data_list, tr_labels_list)
    train_dic = rdimg.to_one_dic(train_dic, d)
# print(train_dic.keys())

# for i in train_dic.keys():
#     print(len(train_dic[i]))

te_data_list, te_labels_list = rdimg.load_image(test_img_path)
test_dic = rdimg.make_the_class_dic(te_data_list, te_labels_list)
# print(test_dic.keys())
# print(len(test_dic[i]))

# print(test_dic[0][0].shape)
# print(type(test_dic[0][0]))
# print(type(test_dic[0][0].shape))

# mark the image, to vector
for i in train_dic.keys():
    tr_vector = []
    for tr_img in train_dic[i]:
        vector = mark.to_vector(tr_img)
        tr_vector.append(vector)
    train_dic[i] = tr_vector
print(train_dic.keys())
print(len(train_dic[0]))
print("========")
print("dic:")
print(type(train_dic[0]))
print("dic_values:")
print(type(train_dic[0][0]))

# choose the network
network = get_net.choose_the_network(time_now, nodes_number, k, p, network_name="watts")



