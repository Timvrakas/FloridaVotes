import csv
import pandas as pd
import logging

def printData(data):
    for county,races in data.items():
        print(county+":")
        for race,parties in races.items():
            print("    "+race+":")
            for party,votes in parties.items():
                print("        " + party + ": "+votes)

def openCSV(date_string):
    logging.log(0,"Opening data file for: " + date_string)
    with open('data//'+date_string+'__fl__general__county__raw.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = {}
        for row in csv_reader:
            division = row["division"]
            office = row["office"]
            party = row["party"]
            votes = row["votes"]
            if division not in data:
                data[division] = dict()
            if office not in data[division]:
                data[division][office] = dict()

            data[division][office][party] = votes
        logging.log(0,str(len(data))+" counties read!")
    return data

def parse():
    race = 'President of the United States'
    race_dates = ["20161108","20121106"]

    data = dict()
    for date in race_dates:
        data[date] = openCSV(date)

    lean = dict()

    for year,year_data in data.items():
        for county,races in year_data.items():
                #print(county+":")
                if county not in lean:
                    lean[county] = dict()
                parties = races[race]
                #print("    "+race+":")
                vote_sum = 0
                for party,votes in parties.items():
                    vote_sum += int(votes)
                    #print("        " + party + ": "+votes)
                #print("        Total Votes: " + str(vote_sum))
                votes_r = int(parties["Republican"])
                votes_d = int(parties["Democrat"])
                votes_diff = ((votes_r-votes_d)/vote_sum)*100
                lean[county][year]=votes_diff
                #print("        R-D Point Difference: %.2f" % votes_diff+"%")
    return lean