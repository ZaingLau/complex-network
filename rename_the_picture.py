import os


def multi_sub_folders(path):
    outer_path = path
    folderlist = os.listdir(outer_path)  # 列举文件夹
    for folder in folderlist:
        inner_path = os.path.join(outer_path, folder)
        # total_num_folder = len(folderlist)  # 文件夹的总数
        # print
        # 'total have %d folders' % (total_num_folder)  # 打印文件夹的总数
        filelist = os.listdir(inner_path)  # 列举图片
        i = 0
        for item in filelist:
            # total_num_file = len(filelist)  # 单个文件夹内图片的总数
            if item.endswith('.jpg'):
                src = os.path.join(os.path.abspath(inner_path), item)  # 原图的地址
                dst = os.path.join(os.path.abspath(inner_path), str(i) + '.jpg')  # 新图的地址（这里可以把str(folder) + '_' + str(i) + '.jpg'改成你想改的名称）
                try:
                    os.rename(src, dst)
                    # print
                    # 'converting %s to %s ...' % (src, dst)
                    i += 1
                except:
                    continue
        # print
        # 'total %d to rename & converted %d jpgs' % (total_num_file, i)
    return 0


def no_sub_folder(path, classname):
    filelist = os.listdir(path)  # 列举图片
    # i = classname * 1000
    i = 0
    for item in filelist:
        # total_num_file = len(filelist)  # 单个文件夹内图片的总数
        if item.endswith('.jpg'):
            src = os.path.join(os.path.abspath(path), item)  # 原图的地址
            dst = os.path.join(os.path.abspath(path), str(i) + '.jpg')
            try:
                os.rename(src, dst)
                # print
                # 'converting %s to %s ...' % (src, dst)
                i += 1
            except:
                continue


for classname in range(4, 10):
    no_sub_folder('E:/mnist_dataset/mnist_dataset/MNIST/raw/train_set/' + str(classname), classname)


