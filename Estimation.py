import csv
import matplotlib.pyplot as plt

with open('Data.csv', mode='r') as file:
    data = csv.reader(file)
    data_2021 = []
    for row in data:
        if row[0] == "Month":
            last_months = row[-6:]
        elif row[0] == "2021":
            data_2021 = row
            sales_2021 = sum([int(x) for x in row[1:7]])
        elif row[0] == "2022":
            sales_2022 = sum([int(x) for x in row[1:7]])

    sales_growth_rate = (sales_2022 - sales_2021) / sales_2022

    estimated_values = []

    i = 0

    for month_value_2021 in [int(x) for x in data_2021[-6:]]:
        month_value_2022 = month_value_2021 + month_value_2021 * sales_growth_rate
        estimated_values.append(month_value_2022)

        with open('stats.txt', mode='a') as stats:
            stats.write(f"{last_months[i]}: {month_value_2022}\n")
        i += 1

x = last_months
y = estimated_values

plt.figure(1)
plt.barh(x, y)

plt.title("Estimated sales for 2022")
plt.xlabel("Month")
plt.ylabel("Estimated sales")
plt.grid()

plt.show()