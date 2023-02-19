import pandas as pd
import csv


def csv_to_list(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data

def list_to_csv(csvlist, filename):
    with open(filename, 'w') as f:
        write = csv.writer(f)
        write.writerows(csvlist)

if __name__ == "__main__":
    l = csv_to_list("./FrontEnd/public/cases.csv")
    newlist = []
    newlist.append(l[0])
    for i in range(1,len(l)):
        if l[i][2] == "California":
            newlist.append(l[i])
    
    list_to_csv(newlist, "./FrontEnd/public/new_cases.csv")
    