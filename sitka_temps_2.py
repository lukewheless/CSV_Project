import csv
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

row = next(csv_file)

low = []
date = []

from datetime import datetime

for row in csv_file:
    low.append(int(row[6]))
    the_date = datetime.striptime(row[2], "%Y-%m-%d")
    date.append(the_date)

import matplotlib.pyplot as plt  

fig = plt.figure()

plt.plot(date, low, c = "blue")
plt.title('Daily High Temp', fontsize = 20)
plt.ylabel('Temperature (F)', fontsize = 18)
plt.tick_params(axis = 'both', labelsize = 16)

fig.autofmt_xdate()

plt.show()






