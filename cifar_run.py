from flex_mnist import read_the_image as rdimg
from flex_mnist import mark_the_image as mark
from flex_mnist import make_the_network as get_net
from flex_mnist import refresh_the_image as fresh
from flex_mnist import cal_the_distance as pdt

import random
import time

time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())

# params
nodes_number = 1024
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

te_data_list, te_labels_list = rdimg.load_image(test_img_path)
test_dic = rdimg.make_the_class_dic(te_data_list, te_labels_list)

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
for i in test_dic.keys():
    te_vector = []
    for te_img in test_dic[i]:
        vector = mark.to_vector(te_img)
        te_vector.append(vector)
    test_dic[i] = te_vector
print(len(test_dic[0][0]))
print("===============")

# choose the network, get degree list
# nodes_number = len(train_dic[train_dic])    # DON'T FORGET TO CHANGE HERE
print("nodes number:" + str(nodes_number))
network = get_net.choose_the_network(time_now, nodes_number, k, p, network_name="watts")
degree_list = network.degree

# divide degree
for i in train_dic.keys():
    for j in range(len(train_dic[i])):
        train_dic[i][j] = fresh.refresh_the_img(train_dic[i][j], degree_list)

# get average
for i in train_dic.keys():
    train_dic[i] = fresh.get_average(train_dic[i])
    # 'train_dic' here should be called 'a standard dictionary with standard list', no more for training
print(train_dic.keys())
print(len(train_dic[0]))
print(train_dic[0][0])

# test_dic
predicts = {}
for i in test_dic.keys():
    predict_list = []
    for j in test_dic[i]:
        predict_list.append(pdt.predict(j, train_dic, function="euclidean"))
    predicts[i] = predict_list
print(predicts.keys())
print(len(test_dic[0]))
print(len(predicts[0]))
print(predicts[0])

# evaluate
class_number = len(test_dic.keys())


