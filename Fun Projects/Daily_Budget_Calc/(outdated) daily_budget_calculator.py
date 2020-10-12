# for the moment, on the initial run, before you have any data to unpickle,
# you need to comment out the 'pickle load' block. once you have the pickle data you can
# uncomment and it will run normally.

# Dependencies
import calendar
from datetime import date
import pickle
import matplotlib.pyplot as plt
import numpy as np

# Setup
today = date.today()
days_of_month = calendar.monthrange(today.year, today.month)
mem_dict = {}
days_remain = (days_of_month[1]) - (today.day - 1)

def d_budget(sum_t):
    daily_budget = (sum_t / days_remain)
    return daily_budget

# pickle load
filename = 'date_budget'
infile = open(filename, 'rb')
mem_dict = pickle.load(infile)
infile.close()

# Front end
print("DAILY BUDGET CALCULATOR")
print("--------------------------")
#print(f'Last run: {mem_dict[-1]}')
print(" ")
print("Today's date:", today)
print("--------------------------")

# User input
total_sum = float(input('How much money do you currently have to budget through the end of the month?: '))
daily_budget = d_budget(total_sum)

# Accumulators
print("--------------------------")
print(f'Assuming you spend no money, here is how your daily budget will accumulate through the end of the month')

total = 0
day = 0
x_day = []
y_total = []
for sol in range(days_remain):
    total = total + daily_budget
    print(f'DAY + {day} AMOUNT: {round(total, 2)}')
    x_day.append(day)
    y_total.append(total)
    day += 1

# Accumulator plot
plt.bar(x_day, y_total)
plt.xticks(np.arange(0, days_remain + 1, 1))
plt.xlabel('Days')
plt.ylabel('Amount Accumulated')
plt.xticks(rotation=45)
plt.show()

# Dictionary update
mem_dict[today] = [round(daily_budget, 2), total_sum]
print(mem_dict)

# x & y values
x_date = []
y_d_value = []
y_t_value = []

for key, value in mem_dict.items():
    x_date.append(key)
    y_d_value.append(value[0])
    y_t_value.append(value[1])

# budget per day over time plot
plt.plot(x_date, y_d_value)
plt.xlabel('Date')
plt.ylabel('Budget/Day over Time')
plt.xticks(rotation=45)

plt.show()

# balance over time plot
plt.plot(x_date, y_t_value)
plt.xlabel('Date')
plt.ylabel('Balance over Time')
plt.xticks(rotation=45)

plt.show()

# pickle store memory
filename = 'date_budget'
outfile = open(filename, 'wb')
pickle.dump(mem_dict, outfile)
outfile.close()
