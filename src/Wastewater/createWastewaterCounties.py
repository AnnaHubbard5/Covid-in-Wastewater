import pandas as pd
from sodapy import Socrata
from datetime import datetime, timedelta
import json



def wwByCounty(county_name, date, limit= None):
    client = Socrata("data.cdc.gov", None)
    results = None
    while not results:  
        results = client.get("2ew6-ywp6", county_names = county_name, date_end = date,limit = limit)
        date = getDayEarlier(date)
    return results

def getAveragePercentage(county_name, date, limit= None):
    results = wwByCounty(county_name, date, limit)
    percentile = 0
    for result in results:
        percentile += result['percentile']

    percentile = percentile / results
        print("hi")

def getDayEarlier(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    prev_day_obj = date_obj - timedelta(days=1)
    prev_day_str = prev_day_obj.strftime("%Y-%m-%d")
    return prev_day_str

def get_dict_from_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data

def populateJson():
    counties = get_dict_from_json("./src/data/california-counties.json")['features']
    for county in counties:
        county_name = county['properties']['name']

    print("h")




if __name__ == "__main__":
    getAveragePercentage("Alameda", "2023-02-18")
    #populateJson()
    #wwByCounty("Alameda", "2023-02-18")