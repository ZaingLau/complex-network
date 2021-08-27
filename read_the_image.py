import pickle
import numpy as np


def load_image(path):
    with open(path, 'rb') as f:
        dataset = pickle.load(f, encoding='latin1')
        # print(dataset['data'].shape)
        # print(dataset.keys())
        data = dataset['data']
        labels = dataset['labels']
        data = np.reshape(data, (10000, 3, 32, 32))
        labels = np.asarray(labels)
        # print(data)
        # print(labels)
    return data, labels


def make_the_class_dic(data_list, labels_list):
    d = {}
    if isinstance(labels_list, np.ndarray):
        labels_list = labels_list.tolist()
    elif type(labels_list) is not np.ndarray or list:
        raise RuntimeError('Wrong type label list')
    if (data_list is None) or (labels_list is None):
        raise RuntimeError('Have blank list')
    labels_list = enumerate(labels_list)
    for i, x in labels_list:
        if x not in d:
            d[x] = []
        index = i
        # print('index:'+str(index))
        data = data_list[index]
        d[x].append(data)
    return d


'''
data_list, labels_list = load_image('E:/cifar-10-python/cifar-10-batches-py/data_batch_1')
print(labels_list)
dic = make_the_class_dic(data_list, labels_list)
print(len(dic[0]))
print(len(dic[1]))
print(len(dic[2]))
print(len(dic[8]))
print(len(dic[9]))
print(dic[0][0])
print(type(dic[0]))
'''


def to_one_dic(dic_set, d):
    for k in d.keys():
        if k not in dic_set:
            dic_set[k] = d[k]
        else:
            dic_set[k] += d[k]
    return dic_set

