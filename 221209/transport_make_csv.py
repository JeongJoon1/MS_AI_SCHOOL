import pandas as pd
import os

train_df_dict = {
    'file_name' : [],
    'label' : []
}
[{'file_name' : ['airplane0']}, {'label' : [0]}]
test_df_dict = {
    'file_name' : [],
    'label' : []
}

labels_map = {
    'airplane' : 0,
    'bicycle' : 1,
    'car' : 2
}

train_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_train_data/'
test_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_test_data/'

train_files = os.listdir(train_dir)
test_files = os.listdir(test_dir)

for train_file in train_files:
    if "airplane" in train_file:
        label = "airplane"
    elif "bicycle" in train_file:
        label = "bicycle"
    elif "car" in train_file:
        label = "car"
    train_df_dict['label'].append(labels_map[label])
    train_df_dict['file_name'].append(train_file)

for test_file in test_files:
    if "airplane" in test_file:
        label = "airplane"
    elif "bicycle" in test_file:
        label = "bicycle"
    elif "car" in test_file:
        label = "car"
    test_df_dict['label'].append(labels_map[label])
    test_df_dict['file_name'].append(test_file)

train_df = pd.DataFrame(train_df_dict)
test_df = pd.DataFrame(test_df_dict)
train_df.to_csv('C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_train_annotations.csv')
test_df.to_csv('C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_test_annotations.csv')