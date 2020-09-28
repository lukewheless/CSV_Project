import csv
open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter = ",")

row = next(csv_file)

'''
print(row)

for i, c in enumerate(row):
    print(i,c)
'''
from datetime import datetime

low = []
high = []
date = []

for row in csv_file:
    try:
        highs = (int(row[4]))
        lows = (int(row[5]))
        the_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {the_date}")
    else:
        high.append(high)
        low.append(low)
        date.append(the_date)

import matplotlib.pyplot as plt  

fig = plt.figure()

plt.plot(date, high, c = "red")
plt.plot(date, low, c = "blue")

plt.title('Death Valley', fontsize = 20)
plt.xlabel('', fontsize = 12)

plt.fill_between(date, high, low, facecolor = "blue", alpha = 0.1)

fig.autofmt_xdate()

plt.show()






