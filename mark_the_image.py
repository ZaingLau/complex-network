# from skimage import io
# import pandas as pd

path = r'E:/mnist_dataset/mnist_dataset/MNIST/raw/'


def transfer_byimg_to_vector(img):
    # size = img.shape[0] * img.shape[1]
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


def multimg_to_vector(img):

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


