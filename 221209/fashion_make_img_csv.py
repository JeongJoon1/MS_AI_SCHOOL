import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import Dataset
from torchvision.io import read_image
import pandas as pd


img_size = 28
num_images = 5

# 바이너리 파일을 img와 label인 csv파일로 변경
imgf = open('data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)
lblf = open('data/FashionMNIST/raw/t10k-labels-idx1-ubyte', 'rb')
lbuf = lblf.read(8)
df_dict = {
    'file_name' : [],
    'label' : []
}
idx = 0
os.mkdir('C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/test_imgs')
while True:
    imgd = imgf.read(img_size*img_size)
    if not imgd:
        break
    data = np.frombuffer(imgd, dtype = np.uint8).astype(float)
    data = data.reshape(1, img_size, img_size, 1)
    image = np.asarray(data).squeeze()
    lbld = lblf.read(1)
    labels = np.frombuffer(lbld, dtype = np.uint8).astype(np.int64)
    file_name = f'{idx}.png'
    cv2.imwrite(f'C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/test_imgs/{file_name}', image)
    idx += 1
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)
# print(df_dict)
import pandas as pd
df = pd.DataFrame(df_dict)
print(df)
df.to_csv('C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/test_annotations.csv')

