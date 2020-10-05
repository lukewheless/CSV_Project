import csv
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

row = next(csv_file)

high = []

for row in csv_file:
    high.append(int(row[5]))
print(high)

from datetime import datetime

high = []
date = []

for row in csv_file:
    high.append(int(row[5]))
    the_date = datetime.striptime(row[2], "%Y-%m-%d")
    date.append(the_date)

import matplotlib.pyplot as plt  

fig = plt.figure()

plt.plot(date, high, c = "red")
plt.title('Daily High Temp', fontsize = 20)
plt.ylabel('Temperature (F)', fontsize = 18)
plt.tick_params(axis = 'both', labelsize = 16)

fig.autofmt_xdate()

plt.show()






