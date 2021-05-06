import tabula
import pandas as pd
import numpy as np
import subprocess
import os

#import pdfs
cwd = os.getcwd()
frames=[]

for filename in os.listdir(cwd):
    if filename.endswith('.pdf'):
        date=[int(i) for i in filename if i.isdigit()]
        date=f'{date[4]}{date[5]}/{date[6]}{date[7]}/{date[0]}{date[1]}{date[2]}{date[3]}'
        df = tabula.read_pdf(filename,pages='all')[0]
        df.insert(0,'date','')
        df['date'] = date
        frames.append(df)

#function formats df with correct column keys, size, and drops empty rows. returns list of formated frames
def format_df (df_list):
    result = []
    for df in df_list:
        df.columns = df.iloc[2]
        df.dropna(how='all', subset=["Company"], inplace=True)
        df.dropna(how='all', axis=1,inplace=True)
        result.append(df)
    return result

#func adds date column with dates based on file name    

new_list = format_df(frames)    
# print(new_list[0])

result = pd.concat(new_list)

excel_output_file = 'testing.xlsx'

# result.to_excel(excel_output_file)

#open file using bash

# subprocess.Popen([excel_output_file],shell=True)