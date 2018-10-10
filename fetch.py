import wget
import urllib
import os

dates = ["20161108","20141104","20121106","20101102","20081104","20061107","20041102","20021105","20001107"]
state_code = "fl"
race = "general"
region_type = "county"


BASE_URL = "https://github.com/openelections/openelections-results-"
filenames = list()

if not os.path.isdir("data"):
    os.mkdir("data")

for date in dates:
    url=BASE_URL+state_code+"/blob/master/raw/"+date+"__"+state_code+"__"+race+"__"+region_type+"__raw.csv?raw=true"
    try:
        filename = wget.download(url,out="data/")
        print("\n\rDownloaded file: %s" % filename)
        filenames += [filename]
    except urllib.error.HTTPError :
        print("Error Downloading File!")
print(filenames)