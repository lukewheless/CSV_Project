import csv
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

row = next(csv_file)

low = []
high = []
date = []

from datetime import datetime

for row in csv_file:
    high.append(int(row[5]))
    low.append(int(row[6]))
    the_date = datetime.strptime(row[2], "%Y-%m-%d")
    date.append(the_date)

import matplotlib.pyplot as plt  

fig = plt.figure()

plt.plot(date, high, c = "red")
plt.plot(date, low, c = "blue")
fig.autofmt_xdate()
plt.ylabel('Temp', fontsize = 20)
plt.xlabel('', fontsize = 12)
plt.fill_between(date, high, low, facecolor = "blue", alpha = 0.1)

plt.show()






