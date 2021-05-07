import tabula
import pandas as pd
import numpy as np
import subprocess
import os

cwd = os.getcwd()


#got file names from pictures. 
photos_files=[]
excel=[]
for filename in os.listdir(cwd):
    if filename.endswith('.jpg' or '.JPG*'):
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

# new_list = format_df(frames)    

# result = pd.concat(new_list)

# excel_output_file = 'new.xlsx'

# result.to_excel(excel_output_file)

#open file using bash

# subprocess.Popen([excel_output_file],shell=True)

#create a dictionary with photo key and id values
df = frames[0]

photos = df['Photos'].values
id = df['Item Number'].values

id_photo={}
for i, photo in enumerate(photos, 0):
    id_photo[photo]=id[i]


for file in photos_files:
   val = id_photo.get(file)
   if val: 
        os.rename(file, f'{val}_{file}' )
