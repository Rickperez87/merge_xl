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
        df.columns = col_names
        df = df.iloc[1:,:]
        #make sure that originator exists col 5
        df.dropna(how='all', subset=df.columns[[5]], inplace=True)
        result.append(df)
    return result
    
col_names=['Description','Area/segment or Building','Specific Location','Technical Requirements', 'Discipline', 'Originator','Remarks','Photos']

new_list = format_df(df_from_xlsx(init_excel_filenames(filenames_list)),col_names)+ format_df(df_from_pdf(init_pdf_filenames(filenames_list)),col_names)

result = pd.concat(new_list)

excel_output_file = 'new.xlsx'

result.to_excel(excel_output_file)

#open file using bash
subprocess.Popen([excel_output_file],shell=True)