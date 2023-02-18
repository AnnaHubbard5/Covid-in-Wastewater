import pandas as pd
from sodapy import Socrata
from datetime import datetime, timedelta



def wwByCounty(county_name, date, limit= None):
    client = Socrata("data.cdc.gov", None)
    results = None
    while not results:  
        results = client.get("2ew6-ywp6", county_names = county_name, date_end = date,limit = limit)
        date = getDayEarlier(date)




def getDayEarlier(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    prev_day_obj = date_obj - timedelta(days=1)
    prev_day_str = prev_day_obj.strftime("%Y-%m-%d")
    return prev_day_str



if __name__ == "__main__":
    wwByCounty("Alameda", "2023-02-18")