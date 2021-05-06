import tabula
import pandas as pd
import numpy as np
import subprocess

# read_pdf will save the pdf table into Pandas Dataframe
pdf_df1 = tabula.read_pdf("DCMP SLY Testing and Inspection Schedule 20210505.pdf", pages='all')[0]
pdf_df2 = tabula.read_pdf("DCMP SLY Testing and Inspection Schedule 20210504.pdf", pages='all')[0]

# load excel into Pandas Dataframe
#df1 = pd.read_excel('N99_WHB_SCI_Findings_IT_NCS.xlsx')

frames=[pdf_df1,pdf_df2]

#function formats df with correct column keys, size, and drops empty rows. returns list of formated frames
def format_df (df_list):
    result = []
    for df in df_list:
        df.columns = df.iloc[2]
        df.dropna(how='all', subset=["Company"], inplace=True)
        df.dropna(how='all', axis=1,inplace=True)
        result.append(df)
    return result
    

new_list = format_df(frames)    
print(new_list[0])

result = pd.concat(new_list)

excel_output_file = 'testing.xlsx'

result.to_excel(excel_output_file)

#open file using bash

subprocess.Popen([excel_output_file],shell=True)