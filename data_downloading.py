import sys
import requests
import numpy as np
import pandas as pd

def cleaning_data(df):
    #Checking for NA values
    print('Prescence of null values is:',df.isnull().values.any())
    df.dropna(inplace=True)
    cols = df.columns.drop(['anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT'])
    df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
    df['age'] = df['age'].astype('int64')
    df[['anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT']]= df[['anaemia', 'diabetes', 'high_blood_pressure', 'sex', 'smoking', 'DEATH_EVENT']].astype(bool)
    #Removing duplicate data
    df.drop_duplicates(keep='first')
    #Removing abnormal data with IDR method
    for col in cols:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        df_cleaned = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
    #Grouping data according to age ranges
    bins = [0, 12, 19, 39, 59, np.inf]
    names = ['Child', 'Teenager', 'Young Adult', 'Adult', 'Elder']
    df_cleaned['AgeRange'] = pd.cut(df_cleaned['age'], bins, labels=names)
    #saving he data in a csv file
    df_cleaned.to_csv('Cleaned_Data.csv',  index=False)


url = sys.argv[1]
response = requests.get(url)
# Check if the response is successful
if response.status_code == 200:
    # Get the file name from the URL
    file_name = url.split('/')[-1]
    # Open a file with the same name as the URL and write the response content
    with open(file_name, 'wb') as file:
        file.write(response.content)
    # Print a success message
    print(f'Downloaded {file_name} from {url}')
else:
    # Print an error message
    print(f'Failed to download from {url}')

df =  pd.read_csv(file_name, na_values=['(NA)'], header=0)
cleaning_data(df)



