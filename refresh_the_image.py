from skimage import io
from flex_mnist import mark_the_image
from flex_mnist import make_the_network
import pandas as pd
import time


def refresh_the_img(list_img, list_degree):
    for i in range(0, len(list_img)):
        list_img[i] = list_img[i] % list_degree[i]
    return list_img


def compute_the_average(img):
    new_img = []
    for i in range(0, len(img[0])):
        vec_sum = 0
        for j in range(0, len(img)):
            vec_sum += img[j][i]
        vec_sum_ave = vec_sum / len(img)
        new_img.append(vec_sum_ave)
    return new_img


def make_standard_image(train_path, train_start, train_end, network):
    refreshed_image = []
    degree_vector = make_the_network.make_the_degree_list(network)
    for i in range(train_start, train_end):
        image = io.imread(train_path + str(i) + '.jpg')
        image_vector = mark_the_image.transfer_byimg_to_vector(image)
        new_image_vector = refresh_the_img(image_vector, degree_vector)
        refreshed_image.append(new_image_vector)
    print("finished")
    standard_image = compute_the_average(refreshed_image)
    return standard_image


def make_standard_list(train_start, train_end, network, *train_path):
    standard_list = []
    time_now = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime())
    for i in range(0, len(train_path)):
        standard_image = make_standard_image(train_path[i], train_start, train_end, network)
        standard_list.append(standard_image)
    df = pd.DataFrame(standard_list)
    df.to_excel("E:/pycharm-program/flex_mnist/model/" + time_now + ".xlsx", header=range(0, len(train_path)), index=False)
    return standard_list

