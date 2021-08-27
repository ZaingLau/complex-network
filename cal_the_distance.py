import numpy as np
import random
from skimage import io
from flex_mnist import mark_the_image
import pandas as pd
import time
import os


def cal_the_euclidean_distance(test_img_list, standard_list):
    sum = 0
    for i in range(0, len(standard_list)):
        x = test_img_list[i]
        y = standard_list[i]
        square = (x - y) * (x - y)
        sum += square
    distance = np.sqrt(sum)
    return distance


def cal_the_other_kinds_of_distance():
    pass


def predict(test_image, standard_list, function=["euclidean", "other"]):
    distance_list = []
    if function == "euclidean":
        for i in range(0, len(standard_list)):
            distance_list.append(cal_the_euclidean_distance(test_image, standard_list[i]))
    elif function == "other":
        print("Haven't been designed")
        # distance_0 = 0
        # distance_1 = 0
    else:
        print("No such function")
        # distance_0 = 0
        # distance_1 = 0

    index_list = []
    result = distance_list.index(min(distance_list))
    index_list.append(result)
    for i in range(0, len(distance_list)):
        if distance_list[i] == distance_list[result]:
            index_list.append(i)
            break
    if len(index_list) > 1:
        result = random.choice(index_list)
    else:
        result = result
    return result


# only used in consecutive image name, if predict several spectacular images, use the function 'predict'
def make_predict_list(file_time, test_path, start, end, standard_list, function=["euclidean", "other"]):
    time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    if not os.path.exists("E:/pycharm-program/flex_mnist/result/" + file_time + "/predict/"):
        os.makedirs("E:/pycharm-program/flex_mnist/result/" + file_time + "/predict/")
    predict_list = []
    for i in range(start, end):
        test_image = io.imread(test_path + str(i) + '.jpg')
        test_image_vector = mark_the_image.transfer_byimg_to_vector(test_image)
        prediction = predict(test_image_vector, standard_list, function=function)
        predict_list.append(prediction)
    df = pd.DataFrame(predict_list)
    df.to_excel("E:/pycharm-program/flex_mnist/result/" + file_time + "/predict/" + time_now + ".xlsx", header=None, index=False)
    return predict_list

