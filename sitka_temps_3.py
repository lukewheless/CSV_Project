import csv
open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

row = next(csv_file)

#for i, c in enumerate(row):
    #print(i,c)

low = []
high = []

date = []
from datetime import datetime
x = datetime.striptime("2010-07-01", "%Y-%m-%d")
print(x)

for row in csv_file:
    high.append(int(row[5]))
    low.append(int(row[6]))
    the_date = datetime.striptime(row[2], "%Y-%m-%d")
    date.append(the_date)

import matplotlib.pyplot as plt  

fig = plt.figure()

# fig, ax = plt.subplots(2,2) 

plt.plot(dates, high, c = "red")
plt.plot(dates, low, c = "blue")
fig.autofmt_xdate()
plt.ylabel('Temp', fontsize = 20)
plt.xlabel('', fontsize = 12)
plt.fill_between(dates, highs, low, facecolor = "blue", alpha = 0.1)

plt.show()






