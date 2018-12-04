import csv
import logging

ocd_num = dict()
num_ocd = dict()
name_num = dict()
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

        ocd = "ocd-division/country:us/state:fl/county:" + name
        county[0] = ocd
        county[1] = "12" + county[1]
        ocd_num[county[0]]=county[1]
        num_ocd[county[1]]=county[0]
        name_num[name]=county[1]

def ocd_to_id(ocd_str):
    if len(county_codes) == 0:#build data if missing
        parse_id_map()
    return ocd_num[ocd_str]

def ocd_to_name(ocd_str):
    return ocd_str[40:]

def id_to_ocd(id_str):
    if len(county_codes) == 0:#build data if missing
        parse_id_map()
    return num_ocd[id_str]

def name_to_num(name_str):
    if len(county_codes) == 0:#build data if missing
        parse_id_map()
    return name_num[name_str]
