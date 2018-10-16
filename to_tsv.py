import pandas as pd
import csv

county_codes = list()

with open('st12_fl_cou.txt', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        county_codes.append(list([row["county"] , row["ct_num"]]))

for county in county_codes:
    name = str(county[0])
    name = name.replace(' County','')
    name = name.lower()
    name = name.replace(' ','_')
    name = "ocd-division/country:us/state:fl/county:" + name
    county[0] = name
    county[1] = "12" + county[1]
#print(county_codes)
    


data = pd.read_pickle("map_data.pkl")
data_dict = data.to_dict()
#print(data_dict)

final_data = list()

final_data.append(["id","2000","2008","2012","2016"])
for county in county_codes:
    if county[0] in data_dict:
        years = list(data_dict[county[0]].values())
        point = [county[1]] + years
        final_data.append(point)

print(final_data)

with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(final_data)
    