import pandas as pd
import csv
from datetime import datetime


def csv_to_list(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def list_to_csv(csvlist, filename):
    with open(filename, 'w') as f:
        write = csv.writer(f)
        write.writerows(csvlist)

def add_epoch(date):
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    epoch_value = int(date_obj.timestamp())
    return epoch_value

if __name__ == "__main__":
    # print(add_epoch("2022-01-01"))
    l = csv_to_list("./FrontEnd/public/new_cases.csv")
    newlist = []
    newlist.append(l[0])
    for i in range(1,len(l)):
        if l[i][2] == "California":
            l[i].append(add_epoch(l[i][11]))
            newlist.append(l[i])
    
    list_to_csv(newlist, "./FrontEnd/public/new_cases.csv")
    