# Exercise 1 - Print current date and time
import datetime

# Print current date and time
print("Current date and time:", datetime.datetime.now())

# Print only current time
print("Current time:", datetime.datetime.now().time())

# Exercise 2 - Convert string into datetime object
from datetime import datetime

date_string = "25 February, 2020"
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("Date object:", date_object)

# Exercise 3 - Subtract a week from a given date
from datetime import datetime, timedelta

given_date = datetime(2020, 2, 25)
print("Given date:", given_date.date())

one_week = timedelta(weeks=1)
new_date = given_date - one_week
print("Date after subtracting a week:", new_date.date())

# Exercise 4 - Format DateTime
from datetime import datetime

now = datetime.now()

# Format the date and time
formatted = now.strftime("%A, %d %B %Y %I:%M %p")
print("Formatted date and time:", formatted)

from datetime import datetime

given_date = datetime(2020, 7, 26)
print(given_date.strftime('%A'))

#Exercise 6 - Add a week and 12 hours to a given date
from datetime import datetime, timedelta
given_date = datetime(2020, 7, 26, 5, 0, 0)
print("Given date and time:", given_date)
days_to_add = timedelta(days=7, hours=12)
new_date = given_date + days_to_add
print("New date and time after adding a week and 12 hours:", new_date)

#Exercise 7 - Print current time in milliseconds
import time
current_time_millis = int(time.time() * 1000)
print("Current time in milliseconds:", current_time_millis)


#Exercise 8 - Convert datetime object to string
from datetime import datetime

given_datetime = datetime(2026, 4, 8, 5, 45, 0)

# Convert the datetime object to a string
formatted_datetime = given_datetime.strftime("%Y-%m-%d %H:%M:%S")
# Print the result and its type
print("Formatted datetime string:", formatted_datetime)
print("Type of formatted datetime:", type(formatted_datetime))


# Exercise 9 - Add 4 months to a given date
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Get current date
current_date = datetime.now().date()

# Add 4 months
new_date = current_date + relativedelta(months=+4)

print("Current date:", current_date)
print("Date after 4 months:", new_date)

# Exercise 10 - Calculate difference between two dates
from datetime import date

# Given dates
date_1 = date(2026, 4, 8)
date_2 = date(2026, 4, 18)

# Difference
delta = date_2 - date_1

print("Number of days:", delta.days)