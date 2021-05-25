import datetime
print("Current date and time", datetime.datetime.now())
print("Current year", datetime.date.today().strftime("%Y"))
print("Current month", datetime.date.today().strftime("%m"))
print("Number of week in the year", datetime.date.today().strftime("%W"))
print("number of weekend in the year", datetime.date.today().strftime("%w"))
print("Day of year: ", datetime.date.today().strftime("%j"))
print("Day of the month : ", datetime.date.today().strftime("%d"))
print("Day of week: ", datetime.date.today().strftime("%A"))