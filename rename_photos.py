import tabula
import pandas as pd
import numpy as np
import subprocess
import os
import re

cwd = os.getcwd()


#got file names from pictures. 
photos_files=[]
filename_no_ext_space=[]
excel=[]
for filename in os.listdir(cwd):
    if filename.endswith('.jpg' or '.JPG*'):
        filename_no_ext_space.append(re.sub('[^A-Za-z0-9]+', '',".".join(filename.split('.')[:-1]).strip().lower()))
        photos_files.append(filename)
    elif filename.endswith('.xlsx'):
        excel.append(filename)
# read_pdf will save the pdf table into Pandas Dataframe
# pdf_df = tabula.read_pdf("Package B SCI Worksheet -WHB - AA.pdf", pages='all')[0]

# # load excel into Pandas Dataframe
frames=[]
for file in excel:
    df=pd.read_excel(file)
    df.columns = df.iloc[0]
    df.dropna(how='all', subset=["Description"], inplace=True)
    df.dropna(how='all', axis=1,inplace=True)
    df.drop([0], inplace=True)
    frames.append(df)

#create a dictionary with photo key and id values
df = frames[0]

df['Photos'] = df['Photos'].str.replace(r'\W','')
photos = df['Photos'].values
photos_no_space=[]
for photo in photos:
    photo=str(photo)
    photos_no_space.append(photo.replace(' ','').lower())
id = df['Item Number'].values

id_photo={}
for i, photo in enumerate(photos_no_space, 0):
    id_photo[photo]=id[i]

for i, file in enumerate(filename_no_ext_space, 0):
    val = id_photo.get(file)
    print(val)
    if val:
        os.rename(photos_files[i], f'{val}_{photos_files[i]}' )
        