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


# torchvision 라이브러리로 데이터셋 다운
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor() # 학습에 바로 사용하기 위해 Tensor로
)

test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)

img_size = 28
num_images = 5
with open('data/FashionMNIST/raw/t10k-images-idx3-ubyte', 'rb') as f:
    a = f.read(16)
    buf = f.read(img_size*img_size*num_images)
    data = np.frombuffer(buf, dtype=np.uint8).astype(float)
    data = data.reshape(num_images, img_size, img_size, 1)
    image = np.asarray(data[1]).squeeze()
    plt.imshow(image, 'gray')
    plt.show()

with open('data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb') as f:
    buf = f.read(num_images)
    labels = np.frombuffer(buf, dtype=np.uint8).astype(np.int64)
    print(labels[2])
    
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",
}

figure = plt.figure(figsize=(8, 8))
cols, rows = 3, 3
for i in range(1, cols * rows + 1):
    sample_idx = torch.randint(len(training_data), size=(1,)).item()
    img, label = training_data[sample_idx]
    figure.add_subplot(rows, cols, i)
    plt.title(labels_map[label])
    plt.axis("off")
    plt.imshow(img.squeeze(), cmap="gray")
plt.show()

# 바이너리 파일을 img와 label인 csv파일로 변경
imgf = open('data/FashionMNIST/raw/train-images-idx3-ubyte', 'rb')
imgd = imgf.read(16)
lblf = open('data/FashionMNIST/raw/train-labels-idx1-ubyte', 'rb')
lbuf = lblf.read(8)
df_dict = {
    'file_name' : [],
    'label' : []
}
idx = 0
os.mkdir('C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/imgs')
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
    cv2.imwrite(f'C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/imgs/{file_name}', image)
    idx += 1
    df_dict['label'].append(labels[0])
    df_dict['file_name'].append(file_name)
# print(df_dict)
import pandas as pd
df = pd.DataFrame(df_dict)
print(df)
df.to_csv('C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/annotations.csv')

