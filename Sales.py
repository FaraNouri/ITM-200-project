import csv
import matplotlib.pyplot as plt

with open('Data.csv', mode='r') as file:
    data = csv.reader(file)
    next(data)
    years = []
    sales = []

    for row in data:
        year = row.pop(0)
        years.append(year)

        total_sales = 0
        for item in row:
            total_sales += int(item)
        sales.append(total_sales)

        with open('stats.txt', mode='a') as stats:
            stats.write(f"{year}: {total_sales}\n")

x = years
y = sales

plt.figure(1)
plt.bar(x, y)

plt.title("Car sales from 2012 to 2022")
plt.xlabel("Years")
plt.ylabel("Total Sales")

plt.show()