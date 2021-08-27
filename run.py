from skimage import io
from flex_mnist import make_the_network
from flex_mnist import refresh_the_image
from flex_mnist import cal_the_distance
from flex_mnist import evaluate
from flex_mnist import tool_functions
import os
import random
import time

# a new dir for new round test
time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
os.makedirs('E:/pycharm-program/flex_mnist/result/' + time_now + '/')

# paths
test_path_by = r'E:/mnist_dataset/mnist_dataset/MNIST/raw/test_by/'
test_path_multi = r'E:/mnist_dataset/mnist_dataset/MNIST/raw/test_multi/'

pair_list = ['0+1', '0+1+2', '0+1+2+3', '0+1+2+3+4', '0+1+2+3+4+5', '0+1+2+3+4+5+6', '0+1+2+3+4+5+6+7',
             '0+1+2+3+4+5+6+7+8', '0+1+2+3+4+5+6+7+8+9']

# params
nodes_number = 784
k = random.randint(2, nodes_number)
p = 0.2

# choose the network
network = make_the_network.choose_the_network(time_now, nodes_number, k, p, network_name="watts")
accuracy_list = []
precision_list = []
sensitivity_list = []
specificity_list = []
f1_score_list = []
auc_list = []

all_standard_list = []
for i in range(0, 10):
    path = 'E:/mnist_dataset/mnist_dataset/MNIST/raw/train_set/' + str(i) + '/'
    filelist = os.listdir(path)
    train_start = 0
    train_end = len(filelist)
    all_standard_list.append(refresh_the_image.make_standard_image(path, train_start, train_end, network))

for test_pair in pair_list:
    class_number = tool_functions.get_the_class_number(test_pair)
    print(class_number)
    test_path = r'E:/mnist_dataset/mnist_dataset/MNIST/raw/test_set/' + test_pair + '/'
    test_start = 0
    test_end = class_number * 1000

    # recalculate image
    standard_list = []
    for i in range(0, class_number):
        standard_list.append(all_standard_list[i])

    print(len(standard_list))

    # predict
    predict_list = cal_the_distance.make_predict_list(time_now, test_path, test_start, test_end, standard_list, function="euclidean")

    # test
    # this part is terminal, if test file changed, this part need to be rewrite
    test_list = []
    for i in range(0, class_number):
         test_list += [i]*1000

    # evaluate
    cm, accuracy, precision, sensitive, specificity, f1_score, auc, label_list = evaluate.cal_confusion_matrix(test_list,
                                                                                                predict_list, class_number)
    accuracy_list.append(accuracy)
    precision_list.append(precision)
    sensitivity_list.append(sensitive)
    specificity_list.append(specificity)
    f1_score_list.append(f1_score)
    auc_list.append(auc)
    evaluate.draw_confusion_matrix(cm, label_list, time_now)
    print("pair_finish")

evaluate.make_the_result_form(accuracy_list, precision_list, sensitivity_list, specificity_list, f1_score_list, auc_list, pair_list, time_now)

