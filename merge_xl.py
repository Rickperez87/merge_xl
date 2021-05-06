import tabula
import pandas as pd
import numpy as np
import subprocess

# read_pdf will save the pdf table into Pandas Dataframe
pdf_df = tabula.read_pdf("Package B SCI Worksheet -WHB - AA.pdf", pages='all')[0]

# load excel into Pandas Dataframe

df1 = pd.read_excel('N99_WHB_SCI_Findings_IT_NCS.xlsx')
df2 = pd.read_excel('Package B SCI Worksheet_WHB.4.27.21-JS.xlsx')
df3 = pd.read_excel('Package B SCI Worksheet-SPeterson.xlsx')
df4 = pd.read_excel('Package B SCI Worksheet-WHB-RS.xlsx')
df5 = pd.read_excel('Package B WHB SCI Worksheet_SBGray.xlsx')

frames = [df2,df3,df4,df5,pdf_df]

#function formats df with correct column keys, size, and drops empty rows. returns list of formated frames
def format_df (df_list):
    result = []
    for df in df_list:

        df = df.iloc[:,1:9]
        df.columns = df.iloc[0]
        df = df.iloc[1:,:]
        df.dropna(how='all', subset=["Originator"], inplace=True)
        result.append(df)
    return result
    

new_list = format_df(frames)    

result = pd.concat(new_list)

excel_output_file = 'new.xlsx'

result.to_excel(excel_output_file)

#open file using bash

subprocess.Popen([excel_output_file],shell=True)