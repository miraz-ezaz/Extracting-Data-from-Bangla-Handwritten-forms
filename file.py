import pandas as pd
import csv


def insertIntoCSV(dict):
    with open('out.csv', 'a+',encoding="utf-8-sig",newline='') as file:
        w = csv.DictWriter(file, dict.keys())

        if file.tell() == 0:
            w.writeheader()

        w.writerow(dict)


