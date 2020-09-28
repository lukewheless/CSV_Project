import csv

from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

row1 = next(csv_file)

low = []
high = []
date = []

for i, temp in enumerate(row1):
    h = row1[5]
    l = row1[6]

for row1 in csv_file:
    high.append(str(h))
    low.append(str(l))

print(low,high)

