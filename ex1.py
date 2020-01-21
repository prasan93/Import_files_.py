import os, random




def get_files():
 selected_files=[]
 for i in range(4):
  r = random.choice(os.listdir("/home/prasan/Desktop/sugeema code/code/New Folder"))#put your path inside "$path "
  if(r not in selected_files):
     selected_files.append(r)
     print(r)
