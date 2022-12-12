import cv2
import numpy as np
import os
from PIL import Image

train_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_train_data/'
test_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_test_data/'

# os.mkdir('C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/resized_transport_train_data/')
# os.mkdir('C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/resized_transport_test_data/')

resized_train_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/resized_transport_train_data/'
resized_test_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/resized_transport_test_data/'

train_files = os.listdir(train_dir)
test_files = os.listdir(test_dir)

for train_file in train_files:
    img = Image.open(train_dir + train_file)
    img_resized = img.resize((28,28))
    img_resized.save(resized_train_dir + train_file)

for test_file in test_files:
    img = Image.open(test_dir + test_file)
    img_resized = img.resize((28,28))
    img_resized.save(resized_test_dir + test_file)

# for test_file in test_files:
#     res = cv2.resize(cv2.imread(train_file), dsize=(28, 28), interpolation=cv2.INTER_CUBIC)
