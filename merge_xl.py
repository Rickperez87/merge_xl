import tabula
import pandas as pd
import numpy as np
import subprocess
import os
import re

cwd = os.getcwd()

# photos_files=[]
filename_no_ext_space=[]
excel=[]
pdf=[]

#create filename_list from folder holding .py file
filenames_list = os.listdir(cwd)

#get file names from pdf and xlsx files
def init_pdf_filenames(filenames_list):
    pdf_files=[]
    filename_no_ext_space=[]
    for filename in filenames_list:
        if filename.endswith('.pdf'):
            pdf_files.append(filename)
            
    return pdf_files

def init_excel_filenames(filenames_list):
    excel=[]
    for filename in filenames_list:
        if filename.endswith('.xlsx'):
            excel.append(filename)
    return excel



# read_pdf will save the pdf table into Pandas Dataframe
# pdf_df = tabula.read_pdf("Package B SCI Worksheet - Train Wash - AA.pdf", pages='all')[0]

# load excel into Pandas Dataframe

# df1 = pd.read_excel('Copy of WMATA Work List - N99 - TWF - SCI Observations. JG - 5.03.21.xlsx')
# df2 = pd.read_excel('Package B SCI Worksheet - TWF - SPeterson.xlsx')
# df3 = pd.read_excel('Package B SCI Worksheet -blank template.xlsx')
# df4 = pd.read_excel('Package B SCI Worksheet -COMMS.xlsx')
# df5 = pd.read_excel('Package B SCI Worksheet -TWF.xlsx')
# df6 = pd.read_excel('SCI inspection- Structural - Train Wash on 5-3-2021.xlsx')

# frames = init_excel_filenames(filenames_list),pdf_df
def df_from_xlsx(excel):
    frames=[]
    for file in excel:
        df=pd.read_excel(file)
        frames.append(df)
    return frames

def df_from_pdf(pdf):
    frames=[]
    for file in pdf:
        df=tabula.read_pdf(file, pages='all')[0]
        frames.append(df)
    return frames

#function formats df with correct column keys, size, and drops empty rows. returns list of formated frames
def format_df (df_list,col_names):
    result = []
    for df in df_list:
        df = df.iloc[:,1:9]
        df.columns = df.iloc[0]
        df = df.iloc[1:,:]
        df.dropna(how='all', subset=df.columns[[6]], inplace=True)
        result.append(df)
    return result
    
col_names=['Item Number','Description','Area/segment or Building','Specific Location','Technical Requirements', 'Discipline', 'Originator','Photos']
# print(init_excel_filenames(filenames_list), 'list....')

new_list = format_df(df_from_xlsx(init_excel_filenames(filenames_list)),col_names)+ format_df(df_from_pdf(init_pdf_filenames(filenames_list)),col_names)


result = pd.concat(new_list)

excel_output_file = 'new.xlsx'

result.to_excel(excel_output_file)

#open file using bash

subprocess.Popen([excel_output_file],shell=True)