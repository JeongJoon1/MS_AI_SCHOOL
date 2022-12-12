import os

data_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/'
airplane_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/airplane/'
bicycle_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/bicycle/'
car_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/car/'

airplane_files = os.listdir(airplane_dir)
bicycle_files = os.listdir(bicycle_dir)
car_files = os.listdir(car_dir)

# os.makedirs('C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_train_data/')
# os.makedirs('C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_test_data/')

train_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_train_data/'
test_dir = 'C:/Users/tim03/OneDrive - inha.edu/MS_AI_SCHOOL/221209/data/transport_test_data/'

idx = 0
for file in airplane_files:
    if idx <= 100:
        os.rename(airplane_dir+file,train_dir+file)
    else:
        os.rename(airplane_dir+file,test_dir+file)
    idx += 1

idx = 0
for file in bicycle_files:
    if idx <= 100:
        os.rename(bicycle_dir+file,train_dir+"bicycle"+file)
    else:
        os.rename(bicycle_dir+file,test_dir+"bicycle"+file)
    idx += 1

idx = 0
for file in car_files:
    if idx <= 100:
        os.rename(car_dir+file,train_dir+"car"+file)
    else:
        os.rename(car_dir+file,test_dir+"car"+file)
    idx += 1


