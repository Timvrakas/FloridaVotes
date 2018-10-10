import csv

def printData(data):
    for county,races in data.items():
        print(county+":")
        for race,parties in races.items():
            print("    "+race+":")
            for party,votes in parties.items():
                print("        " + party + ": "+votes)

with open('data//20161108__fl__general__county__raw.csv', mode='r') as csv_file:
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

    print(str(len(data))+" counties read!")
    #printData(data)

race = 'President of the United States'

for county,races in data.items():
        print(county+":")
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
        print("        R-D Point Difference: %.2f" % votes_diff+"%")
                