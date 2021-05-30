import pandas as pd
import numpy as np
import subprocess


pattern = input('type string pattern to be repeated:')
start = input('start number:')
end = input('end number:')

#code to create repeated text comma seperated
def repeating_string(pattern,start,end):
    result=[]
    for num in range(int(start), (int(end)+1)):
        result.append(f'{pattern}{num}.jpg')
    return ', '.join(result)
    
# in future make prompt user for input instead of hard coding

result = {'data': [repeating_string(pattern, start, end)]}

# create a data frame
df = pd.DataFrame(result)
print (df)    

excel_output_file = 'output.xlsx'

df.to_excel(excel_output_file)

#open file using bash

subprocess.Popen([excel_output_file],shell=True)