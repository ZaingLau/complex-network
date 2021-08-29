from skimage import io
from flex_mnist import mark_the_image
from flex_mnist import make_the_network
import pandas as pd
import time


def refresh_the_img(img, degree):
    # for single image, both 'img' and 'degree' are vectors
    # ADD Exception HANDLING WAYS HERE
    for i in range(0, len(img)):
        img[i] = img[i] % degree[i]
    return img


def get_average(img_list):
    # Image in list SHOULD BE vectors, not origin image in ndarray type
    # A series of img in, under one key
    if img_list is None:
        raise RuntimeError("Average Error: no image in list")
    ave_img = []
    img_size = len(img_list[0])
    for i in range(img_size):
        px_sum = 0
        for j in range(len(img_list)):
            px_sum += img_list[j][i]
        px_ave = px_sum / len(img_list)
        ave_img.append(px_ave)
    return ave_img


def make_standard_image(train_path, train_start, train_end, network):
    refreshed_image = []
    degree_vector = make_the_network.make_the_degree_list(network)
    for i in range(train_start, train_end):
        image = io.imread(train_path + str(i) + '.jpg')
        image_vector = mark_the_image.transfer_byimg_to_vector(image)
        new_image_vector = refresh_the_img(image_vector, degree_vector)
        refreshed_image.append(new_image_vector)
    print("finished")
    standard_image = get_average(refreshed_image)
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

