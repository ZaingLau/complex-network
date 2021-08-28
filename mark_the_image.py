# from skimage import io
# import pandas as pd
import numpy as np

def transfer_byimg_to_vector(img):
    # 'img' SHOULD BE a 'numpy.ndarray' type
    # CAN COMPLETE: HOW to deal when 'img' is NOT 'numpy.ndarray' type
    vector = []
    axe_i = 0
    axe_j = 0
    for i in range(0,int((img.shape[0])/2)):
        for j in range(0,img.shape[1]):
            vector.append(img[axe_i][axe_j])
            axe_j += 1
        axe_i += 1
        axe_j -= 1
        for j in range(0,img.shape[1]):
            vector.append(img[axe_i][axe_j])
            axe_j -= 1
        axe_i += 1
        axe_j += 1
    return vector


# Here we list the image into 1d directly, without average the layers
def multimg_to_vector(img):
    pass


def to_vector(img):
    if type(img) is not np.ndarray:
        raise RuntimeError("Reading Error, Not an array image.")
    img_shape = img.shape
    if len(img_shape) == 3:
        new_img = []
        # DEFAULT LAYER NUM IS MIN HERE, NEED REWRITE
        layer_index = img_shape.index(min(img_shape))
        if layer_index != 0:
            img_scale = img_shape[0:layer_index] + img_shape[layer_index+1:]
        else:
            img_scale = img_shape[1:]
        if len(img_scale) == 2:
            for i in range(0, img_scale[0]):
                line = []
                for j in range(0, img_scale[1]):
                    new_point_value = 0
                    for k in range(0, img_shape[layer_index]):
                        if layer_index == 0:
                            new_point_value += img[k][i][j]
                        elif layer_index == 1:
                            new_point_value += img[i][k][j]
                        else:
                            new_point_value += img[i][j][k]
                    line.append(new_point_value)
                new_img.append(line)
        elif len(img_shape) != 2:
            # NEED COMPLETED: how trans when img is a MULTI D shape image
            pass
        new_img = np.array(new_img)
    if len(img_shape) == 2:
        new_img = img
    # print("shape:")
    # print(new_img.shape)
    vector = transfer_byimg_to_vector(new_img)
    return vector


# image = io.imread(path + '0_1k/train/1.jpg')
# print(image.shape[0])


'''
images = []
for i in range(0,800):
    image = io.imread(path + '0_1k/train/' + str(i) + '.jpg')
    new_vector = transfer_byimg_to_vector(image)
    images.append(new_vector)

print(len(images))
print(len(images[0]))
print(len(images[1]))
'''

'''
image = io.imread(path + '0_1k/train/0.jpg')

df = pd.DataFrame(image)
df.to_excel("C:/Users/Lenovo/Desktop/image.xlsx", index=False)

df = pd.DataFrame(images)
df.to_excel("C:/Users/Lenovo/Desktop/images.xlsx", index=False)

print(image.shape)
print(len(images[1]))
'''


def transfer_vector_to_byimg(vector):
    img = []
    axe_i = 0
    axe_j = 0
    for i in range(0,int((img.shape[0])/2)):
        for j in range(0,img.shape[1]):
            vector.append(img[axe_i][axe_j])
            axe_j += 1
        axe_i += 1
        axe_j -= 1
        for j in range(0,img.shape[1]):
            vector.append(img[axe_i][axe_j])
            axe_j -= 1
        axe_i += 1
        axe_j += 1


