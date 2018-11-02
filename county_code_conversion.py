import csv
import logging

ocd_to_num = dict()
num_to_ocd = dict()
county_codes = list()

def parse_id_map(): #This helper fuction builds a set of symetric OCD<=>ID Number lookup tables
    #currently it only works for flordia, but it would be good to have it work for anything in the future
    logging.debug("Building OCD<=>ID lookup tables")
    with open('st12_fl_cou.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            county_codes.append(list([row["county"], row["ct_num"]]))

    for county in county_codes:
        name = str(county[0])
        name = name.replace(' County', '')
        name = name.lower()
        name = name.replace(' ', '_')
        name = "ocd-division/country:us/state:fl/county:" + name
        county[0] = name
        county[1] = "12" + county[1]
        ocd_to_num[county[0]]=county[1]
        num_to_ocd[county[1]]=county[0]

def ocd_to_id(ocd_str):
    if len(county_codes) == 0:#build data if missing
        parse_id_map()
    return ocd_to_num[ocd_str]

    
def id_to_ocd(id_str):
    if len(county_codes) == 0:#build data if missing
        parse_id_map()
    return num_to_ocd[id_str]
