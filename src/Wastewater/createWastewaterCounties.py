import pandas as pd
from sodapy import Socrata
from datetime import datetime, timedelta
import json



def wwByCounty(county_name, date, limit= None):
    client = Socrata("data.cdc.gov", None)
    results = None
    i = 0
    while not results and i < 30:  
        results = client.get("2ew6-ywp6", county_names = county_name, date_end = date,limit = limit)
        date = getDayEarlier(date)
        i += 1
    return results

def getAveragePercentage(county_name, date, limit= None):
    results = wwByCounty(county_name, date, limit)
    if not results:
        return -1
    percentile = 0
    for result in results:
        percentile += float(result['percentile'])

    percentile = percentile / len(results)
    return percentile


def getDayEarlier(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    prev_day_obj = date_obj - timedelta(days=1)
    prev_day_str = prev_day_obj.strftime("%Y-%m-%d")
    return prev_day_str

def get_dict_from_json(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data
    
def write_dict_to_json(big_dict, file_name):
    with open(file_name, 'w') as fp:
        json.dump(big_dict, fp)


def populateJson(date):
    counties = get_dict_from_json("./src/data/california-counties.json")['features']
    for i in range(0, len(counties)):
        county_name = counties[i]['properties']['name']
        percentile = getAveragePercentage(county_name, date)
        counties[i]['properties']['percentile'] = percentile
    
    write_dict_to_json(counties, "./src/data/california-counties-prop.json")
    print("h")




if __name__ == "__main__":
    #getAveragePercentage("Alameda", "2023-02-18")
    populateJson("2023-02-18")
    #wwByCounty("Alameda", "2023-02-18")