import csv
from datetime import datetime
import matplotlib.pyplot as plt  

open_file1 = open("sitka_weather_07-2018_simple.csv", "r")
open_file2 = open("death_valley_2018_simple.csv", "r")
csv_file1 = csv.reader(open_file1, delimiter = ",")
csv_file2 = csv.reader(open_file2, delimiter = ",")
row1 = next(csv_file1)
row2 = next(csv_file2)

for i, c in enumerate(row1):
    if c == "TMIN":
        l = c
    elif c == "TMAX":  
        h = c
    elif c == "DATE":
        d = c

low = []
high = []
date = []

for row1 in csv_file1:
    high.append(h)
    low.append(l)
    the_date = datetime.strptime(d, "%Y-%m-%d")
    date.append(the_date)

for row2 in csv_file2:
    try:
        highs = (h)
        lows = (l)
        the_date = datetime.strptime(d, "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {the_date}")
    else:
        high.append(h)
        low.append(l)
        date.append(the_date)

fig, ax = plt.subplots(2,2,sharex = True) 

plt.plot(date, high, c = "red")
plt.plot(date, low, c = "blue")
plt.fill_between(date, high, low, facecolor = "blue", alpha = 0.1)
ax[2].xlabel('Sitka Airport, AK US', fontsize = 20)
ax[1].xlabel('Death Valley, CA US', fontsize = 20)
fig.autofmt_xdate()

fig.show()