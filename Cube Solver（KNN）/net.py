import os
import cv2
from sklearn.neural_network import MLPClassifier
import tools

"""
shape of image is 36*64*3, which is 6912 reshaped into vector

"""

data_dir = './training_set/'
class_names = [
                "Black",
                "White",
                "Red",
                "Green",
                "Blue",
                "Orange",
                "Yellow",
                "Purple",
              ]


if os.path.isdir(data_dir):
    print('训练数据集已找到！')
else:
    print('没有训练数据集！')


def learn():
    print('加载数据集进行学习！')
    n_files = 0
    training_set = list()
    training_labels = list()
    for file in os.listdir(data_dir):
        if file.endswith(".jpg") or file.endswith("png"):
            img_file = os.path.join(data_dir, file)
            label_name = str(file).split('_')
            training_set.append(cv2.imread(img_file, 1).reshape(6912))
            training_labels.append(label_name[0])
            n_files += 1
    
    x = training_set
    y = tools.integerize(training_labels)

    net = MLPClassifier()

    print('\n学习中...\n')
    net.fit(x, y)

    print('MLP已经完成学习!')
    return net


def identify_color(src_image, net):
    image_reshape = src_image.reshape(1, 6912)
    p = net.predict(image_reshape)

    return str(class_names[int(p)])


