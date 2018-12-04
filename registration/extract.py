import csv
import pandas as pd
import numpy as np
from county_code_conversion import name_to_num


def remove_whitespace(x):
    try:
        return x.strip()
    except AttributeError:
        return x


df_2012 = pd.read_csv("2012.csv", index_col=0)
df_2014 = pd.read_csv("2014.csv", index_col=0, header=0,
                      usecols=(lambda x: not x.startswith('Unnamed')))
df_2016 = pd.read_csv("2016.csv", index_col=0)
df_2018 = pd.read_csv("2018.csv", index_col=0)

df_2012.index = df_2012.index.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')
df_2014.index = df_2014.index.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')
df_2016.index = df_2016.index.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')
df_2018.index = df_2018.index.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')

df_2012.columns = df_2012.columns.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')
df_2014.columns = df_2014.columns.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')
df_2016.columns = df_2016.columns.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')
df_2018.columns = df_2018.columns.str.strip().str.lower().str.replace(
    ' ', '_').str.replace('(', '').str.replace(')', '')

frames = [df_2012, df_2014, df_2016, df_2018]


df_2016 = df_2016.applymap(remove_whitespace)

keys = ['2012', '2014', '2016', '2018']

result = pd.concat(frames, keys=keys, axis=0, sort=True)

result.columns = result.columns.str.split('_', expand=True)

result = result.drop(['total'],axis=1).drop(columns='total',level=1)
result.index.names = ['year','county']
result.columns.names = ['group','party']

#print(result)

#slicey = result.loc[(slice(None),'bay'), slice(None)]
#print(slicey)



data = pd.DataFrame(columns=['year','county','group', 'party','id','count'])

for row_index,row in result.iterrows():
    county_id = name_to_num(row_index[1])
    for col_index,col in row.iteritems():
        try:
            count = int(float(str(col).replace(',', '')))
        except Exception as e:
            print(e,end=': ')
            print(col)
            count = 0

        entry = pd.DataFrame([[row_index[0],row_index[1],col_index[0],col_index[1],county_id,count]], columns=['year','county','group','party','id','count'])
        data = data.append(entry)
        
data = data.reset_index(drop=True)

print(data)


data.to_pickle("./data.pkl")
