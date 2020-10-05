import csv
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt  

open_file1 = open("sitka_weather_07-2018_simple.csv", "r")
open_file2 = open("death_valley_2018_simple.csv", "r")
csv_file1 = csv.reader(open_file1, delimiter = ",")
csv_file2 = csv.reader(open_file2, delimiter = ",")
row1 = next(csv_file1)
row2 = next(csv_file2)

for i, c in enumerate(row1):
    if c == "TMIN":
        l = i
    elif c == "TMAX":  
        h = i
    elif c == "DATE":
        d = i

low = []
high = []
date = []

for row1 in csv_file1:
    high.append(int(row1[h]))
    low.append(int(row1[l]))
    the_date = datetime.strptime(row1[d], "%Y-%m-%d")
    date.append(the_date)

low1 = []
high1 = []
date1 = []

for row2 in csv_file2:
    try:
        highs = int(row2[h])
        lows = int(row2[l])
        the_date2 = datetime.strptime(row2[d], '%Y-%m-%d')
    except ValueError:
        print(f"Missing data for {the_date2}")
    else:
        high1.append(highs)
        low1.append(lows)
        date1.append(the_date2)

fig, ax = plt.subplots(2,1) 

fig.suptitle("Temperature Comparison Between Sitka Airport, AK US and Death Valley, CA US", fontsize = 20)

ax[0].set_title('Sitka Airport, AK US', fontsize = 20)
ax[0].plot(date, high, c = "red")
ax[0].plot(date, low, c = "blue")
ax[0].fill_between(date, high, low, facecolor = "blue", alpha = 0.1)

ax[1].set_title('Death Valley, CA US', fontsize = 20)
ax[1].plot(date1, high1, c = "red")
ax[1].plot(date1, low1, c = "blue")
ax[1].fill_between(date1, high1, low1, facecolor = "blue", alpha = 0.1)

fig.autofmt_xdate()
plt.show()