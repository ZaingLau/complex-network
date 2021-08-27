from torchvision import datasets, transforms
import os
from skimage import io
import struct
import numpy as np


# download the data
'''
train_dataset = datasets.MNIST(root, train=True,
                                download=True)
test_dataset =  datasets.MNIST(root, train=False,
                                download=True)
'''


def mnist_load_img(img_path):
    with open(img_path, "rb") as fp:
        # >是以大端模式读取，i是整型模式，读取前四位的标志位，
        # unpack()函数：是将4个字节联合后再解析成一个数，(读取后指针自动后移)
        msb = struct.unpack('>i', fp.read(4))[0]
        # 标志位为2051，后存图像数据；标志位为2049，后存图像标签
        if msb == 2051:
            # 读取样本个数60000，存入cnt
            cnt = struct.unpack('>i', fp.read(4))[0]
            # rows：行数28；cols：列数28
            rows = struct.unpack('>i', fp.read(4))[0]
            cols = struct.unpack('>i', fp.read(4))[0]
            imgs = np.empty((cnt, rows, cols), dtype="int")
            for i in range(0, cnt):
                for j in range(0, rows):
                    for k in range(0, cols):
                        # 16进制转10进制
                        pxl = int(hex(fp.read(1)[0]), 16)
                        imgs[i][j][k] = pxl
            return imgs
        else:
            return np.empty(1)


def mnist_load_label(label_path):
    with open(label_path, "rb") as fp:
        msb = struct.unpack('>i', fp.read(4))[0];
        if msb == 2049:
            cnt = struct.unpack('>i', fp.read(4))[0];
            labels = np.empty(cnt, dtype="int");
            for i in range(0, cnt):
                label = int(hex(fp.read(1)[0]), 16);
                labels[i] = label;
            return labels;
        else:
            return np.empty(1);


def change_image_type(img):
    # img = np.array(img, dtype='uint8')
    img = img.astype('uint8')
    return img


x_train = mnist_load_img("train-images-idx3-ubyte")
y_train = mnist_load_label("train-labels-idx1-ubyte")
print(y_train)
# print(x_train)
print(y_train.size)
print(x_train.dtype)
print(x_train.shape)
x_train = change_image_type(x_train)
print(x_train.dtype)
print(x_train.shape)

for m in range(2, 10):
    j = 0
    for i in range(0, y_train.size):
        if y_train[i] == m:
            img = x_train[i]
            io.imsave('E:/mnist_dataset/mnist_dataset/MNIST/raw/' + str(m) + '/' + str(j) + '.jpg', img)
            j += 1


'''
# 按图片标签的不同，打印MNIST数据集的图片存入不同文件夹下
for i in range(0, 50):
    path = "E:/pycharm-program/wuenda/data/data_a/" + str(y_train[i]) +"/"
    name = str(i)+".png"
    mnist_save_img(x_train[i], path, name)
'''
