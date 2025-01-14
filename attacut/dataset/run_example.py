from create_train_dataset import *

dataset =  '\n'.join([build(i) for i in load_dataset_txt("example.txt")]).strip()

with open("training.txt","w") as f:
  f.write(dataset)
