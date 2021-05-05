import tabula
import pandas as pd
import numpy as np

# read_pdf will save the pdf table into Pandas Dataframe
# pdf_df = tabula.read_pdf("DCMP SLY Testing and Inspection Schedule 20210503.pdf", pages='all')[0]

# pdf_df.columns = pdf_df.iloc[2,:]

# load excel into Pandas Dataframe

#write a function that detects row with first empty row.


# return df sliced to first empty row

df1 = pd.read_excel('N99_WHB_SCI_Findings_IT_NCS.xlsx')
df2 = pd.read_excel('Package B SCI Worksheet_WHB.4.27.21-JS.xlsx')
df3 = pd.read_excel('Package B SCI Worksheet-SPeterson.xlsx')
df4 = pd.read_excel('Package B SCI Worksheet-WHB-RS.xlsx')
df5 = pd.read_excel('Package B WHB SCI Worksheet_SBGray.xlsx')

frames = [df1,df2,df3,df4,df5]

# print(df2.iloc[100])

def format_df (df_list):
    result = []
    for df in df_list:

        df = df.iloc[:,2:9]
        df.columns = df.iloc[0]
        df = df.iloc[1:,:]
        df.dropna(how='all', subset=["Originator"], inplace=True)
        result.append(df)
    return result
    
    # print(df.shape)
    # print(df.columns)
    # print(df.head)

new_list = format_df(frames)    

result = pd.concat(new_list)

result.to_excel('new.xlsx')