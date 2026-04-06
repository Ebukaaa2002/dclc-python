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