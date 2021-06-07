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
        try:
            date=f'{date[4]}{date[5]}/{date[6]}{date[7]}/{date[0]}{date[1]}{date[2]}{date[3]}'
        except IndexError:
            date = f'{date[4]}{date[5]}/0{date[6]}/{date[0]}{date[1]}{date[2]}{date[3]}'
            print(date)
        df = tabula.read_pdf(filename,pages='all')[0]
        df.columns = df.iloc[2]
        df.insert(0,'date_name',date)
        df.dropna(how='all', subset=["Company"], inplace=True)
        df.dropna(how='all', axis=1,inplace=True)
        df.drop([0,2], inplace=True)
        frames.append(df)

#function formats df with correct column keys, size, and drops empty rows. returns list of formated frames, adds date column with dates based on file name    

combined_pdf = pd.concat(frames)

output_filename = 'testing.xlsx'

combined_pdf.to_excel(output_filename)

#open file using bash

subprocess.Popen([output_filename],shell=True)