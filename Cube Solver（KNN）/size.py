import os
import cv2
import uuid

filename = os.listdir("./test")
base_dir = "./test/"
new_dir = "./output/"
size_m = 64
size_n = 36

training_labels = []

for i in range(0,20):
    for file in filename:
        if file.endswith(".jpg") or file.endswith("png"):
            image = cv2.imread(base_dir + file)
            label_name = str(file).split('_')
            image_size = cv2.resize(image,(size_m, size_n))
            cv2.imwrite((new_dir + label_name[0] + '_' + str(uuid.uuid4()) + '.jpg'), image_size)
