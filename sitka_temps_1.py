import csv
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

row = next(csv_file)
'''
print(row)

for i, c in enumerate(row):
    print(i,c)
'''
high = []

for row in csv_file:
    high.append(int(row[5]))
print(high)
from datetime import datetime
high = []
date = []

x = datetime.striptime("2010-07-01", "%Y-%m-%d")
print(x)

for row in csv_file:
    high.append(int(row[5]))
    the_date = datetime.striptime(row[2], "%Y-%m-%d")
    date.append(the_date)

import matplotlib.pyplot as plt  

fig = plt.figure()

plt.plot(dates, high, c = "red")
plt.title('Daily High Temp', fontsize = 20)
plt.ylabel('Temperature (F)', fontsize = 18)
plt.tick_params(axis = 'both', labelsize = 16)

fig.autofmt_xdate()

plt.show()






