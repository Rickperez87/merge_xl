
import pandas as pd
import os
import re
import difflib

cwd = os.getcwd()


photos_files=[]
filename_no_ext_space=[]
excel=[]

#create filename_list from folder holding .py file
filenames_list = os.listdir(cwd)

#get file names from pictures and excel.
def init_jpg_filenames(filenames_list):
    photos_files=[]
    filename_no_ext_space=[]
    for filename in filenames_list:
        if filename.endswith('.jpg' or '.JPG*'):
            photos_files.append(filename)
            filename_no_ext_space.append(remove_spaces_special_chars(filename))
    return [photos_files, filename_no_ext_space]

def init_excel_filenames(filenames_list):
    excel=[]
    for filename in filenames_list:
        if filename.endswith('.xlsx'):
            excel.append(filename)
    return excel

def remove_spaces_special_chars(str):    
    str_no_ext = ".".join(str.split('.')[:-1]).strip().lower() #remove extension ie. '.jpg'
    return re.sub('[^A-Za-z0-9]+', '',str_no_ext)

#run functions
photos_files, filename_no_ext_space = init_jpg_filenames(filenames_list)
excel = init_excel_filenames(filenames_list)

# load excel into Pandas Dataframe
frames=[]
for file in excel:
    df=pd.read_excel(file)
    df.columns = df.iloc[0]
    df.dropna(how='all', subset=["Description"], inplace=True)
    df.dropna(how='all', axis=1,inplace=True)
    df.drop([0], inplace=True)
    frames.append(df)

#create a dictionary with photo key and id values
df = frames[0]

photos = df['Photos'].values
photos_no_space=[]
for photo in photos:
    photo=str(photo)
    photos_no_space.append(photo.replace(' ','').lower())
id = df['Item Number'].values

id_photo={}
for i, photo in enumerate(photos, 0): #change photos no space eto photos and in dict change to remove spaces and special characters.
    photo = str(photo)
    if ',' in photo:
        
        for individual_photo_file in photo.split(','):
            id_photo[individual_photo_file]=id[i]
    else:
        id_photo[photo]=id[i]

#loop through dictionary to remove any nonalpha chars

temp={}
for k,v in id_photo.items():
    new_key = re.sub('[^A-Za-z0-9]+', '',k)
    new_key.strip().lower()
    temp[new_key]=v

id_photo=temp

for i, file in enumerate(filename_no_ext_space, 0):
    #logic here to match filename with closest match to id_photo
    if file[0]=='d': continue
    else:
        result = difflib.get_close_matches(file,id_photo.keys(),1,.9)

        if result:
            print('file is:', file, 'result:',result)
            val = id_photo.get(result[0])
        else: 
            val=False
    
    if val:
        # print('id is:',val)
        # os.rename(photos_files[i], f'{val}_{photos_files[i]}' )
        pass
        