import pandas as pd
import os

df_dict = {
    'file_name' : [],
    'label' : []
}

test_df_dict = {
    'file_name' : [],
    'label' : []
}

labels_map = {
    'airplane' : 0,
    'bicycle' : 1,
    'car' : 2
}

data_dir = 'C:/Users/joon/Github/MS_AI_SCHOOL/221209/data'



for k, v in labels_map.items():
    file_list = os.listdir(data_dir + "/" + k)
    for i in file_list:
        name, t = i.split(".")
        name = int(name)
        if name < 100:
            df_dict['label'].append(v)
            df_dict['file_name'].append(k + "/" + i)
        else:
            test_df_dict['label'].append(v)
            test_df_dict['file_name'].append(k + "/" + i)

print(df_dict)
df = pd.DataFrame(df_dict)
test_df = pd.DataFrame(test_df_dict)
df.to_csv('C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/transport_annotations.csv')
test_df.to_csv('C:/Users/joon/Github/MS_AI_SCHOOL/221209/data/FashionMNIST/transport_test_annotations.csv')