import pandas as pd
import numpy as np
import subprocess




#code to create repeated text comma seperated
def repeating_string(pattern,start,end):
    result=[]
    for num in range(start, (end+1)):
        result.append(f'{pattern}{num}')
    return ', '.join(result)
    
# in future make prompt user for input instead of hard coding
input = 'Train Wash-_TRUC_8-'
start=1
end=6
result = {'data': [repeating_string(input, start, end)]}

# create a data frame
df = pd.DataFrame(result)
print (df)    

excel_output_file = 'output.xlsx'

df.to_excel(excel_output_file)

#open file using bash

subprocess.Popen([excel_output_file],shell=True)