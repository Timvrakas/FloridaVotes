import pandas as pd
import csv
from county_code_conversion import ocd_to_id

def export_for_viz(data_dict):

    final_data = list()
    final_data.append(["id","2016","2012","4"])

    for county in data_dict.keys():
        years = list(data_dict[county].values())
        point = [ocd_to_id(county)] + years
        diff = point[1]-point[2]
        point.append(diff)
        final_data.append(point)

    print(final_data)

    with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(final_data)
    