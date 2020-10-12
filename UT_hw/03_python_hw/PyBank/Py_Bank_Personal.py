import os
import csv
import datetime

input_file = r'C:\Users\fitzp\Desktop\UTDataViz\class_demo\UT-MCC-DATA-PT-01-2020-U-C\homework-instructions\03-Python\Instructions\PyBank\Resources\budget_data.csv'
output_file = r'C:\Users\fitzp\Desktop'

month_count = 0
month_change = []
net_list = []
delta_gain = ["", 0]
delta_loss = ["", 9999999999999999999]
net_total = 0

current_date = datetime.datetime.today()

with open(input_file) as data:
    reader = csv.reader(data)

    header = next(reader)
    first_row = next(reader)
    month_count = month_count + 1
    net_total = net_total + int(first_row[1])
    net_prev = int(first_row[1])

    for row in reader:
        # totals
        month_count += 1
        net_total = net_total + int(first_row[1])

        # deltas
        net_change = int(row[1]) - net_prev
        net_prev = int(row[1])
        net_list = net_list + [net_change]
        month_change = month_change + [row[0]]

        if net_change > delta_gain[1]:
            delta_gain[0] = row[0]
            delta_gain[1] = net_change
        if net_change < delta_loss[1]:
            delta_loss[0] = row[0]
            delta_loss[1] = net_change

net_average = sum(net_list) / len(net_list)

statement = (
    f"Financial Analysis - {current_date}\n"
    f"=============================================\n"
    f"Total Months: {month_count}\n"
    f"Total: ${net_total:.2f}\n"
    f"Average  Change: ${net_average:.2f}\n"
    f"Greatest Increase in Profits: {delta_gain[0]} ($ +{delta_gain[1]:.2f})\n"
    f"Greatest Decrease in Profits: {delta_loss[0]} ($ {delta_loss[1]:.2f})\n"
)

print(statement)

with open(output_file, "w") as analysis_txt:
    analysis_txt.write(statement)
