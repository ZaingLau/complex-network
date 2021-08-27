from flex_mnist import read_the_image as rdimg


train_dic = {}
for i in range(1,6):
    tr_data_list, tr_labels_list = rdimg.load_image('E:/cifar-10-python/cifar-10-batches-py/data_batch_' + str(i))
    d = rdimg.make_the_class_dic(tr_data_list, tr_labels_list)
    train_dic = rdimg.to_one_dic(train_dic, d)
'''
print(train_dic.keys())
for i in train_dic.keys():
    print(len(train_dic[i]))
'''
te_data_list, te_labels_list = rdimg.load_image('E:/cifar-10-python/cifar-10-batches-py/test_batch')
test_dic = rdimg.make_the_class_dic(te_data_list, te_labels_list)
print(test_dic.keys())
print(len(test_dic))
for i in test_dic.keys():
    print(len(test_dic[i]))
print(test_dic[0][0].shape)
print(type(test_dic[0][0].shape))


