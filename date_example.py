import os
from datetime import date as Date
from datetime import datetime
# import time

'''
The codes for time and date depend on the format of the time or date value. Here are some examples:

%Y: year as a 4-digit number (e.g., 2021)
%m: month as a 2-digit number (e.g., 01 for January)
%d: day as a 2-digit number (e.g., 01)
%H: hour as a 2-digit number in 24-hour format (e.g., 13 for 1:00 PM)
%M: minute as a 2-digit number (e.g., 59)
%S: second as a 2-digit number (e.g., 59)

These codes can be used in a format string to specify how a time or date value should be formatted when it is printed. For example, the format string "%Y-%m-%d %H:%M:%S" could be used to print a date and time value as "2021-01-01 13:59:59".'''


def calc_days(month, day, year):
    # Calculate the date object for the given date
    date1 = Date(year, month, day)

    # Calculate the date object for today's date
    date2 = Date.today()

    # Calculate the difference between the two dates in days
    delta = date2 - date1

    # Return the number of days
    return delta.days


os.system('cls')

print(datetime.now())                                       # print date and time - unformatted
print(datetime.now().strftime("%A, %d %b %Y, kl. %X"))      # format Monday, 12 dec 2022, kl. 10:07:07 
print(datetime.now().strftime("%A, %d %b %Y, kl. %X"))      # format 10:00 2022-12-12

date = datetime(2022, 12, 12)

print(date.strftime("%B"))


'''
# Start the stopwatch
start_time = time.time()

# Perform some operation that you want to measure
while True:
    os.system('cls')
    
    # Get the current time
    current_time = time.time()

    # Calculate the elapsed time
    elapsed_time = current_time - start_time

    # Check that elapsed_time is a valid value
    if elapsed_time < 0:
        # elapsed_time is invalid, set it to 0
        elapsed_time = 0

    # Convert elapsed_time to a time tuple
    elapsed_time_tuple = time.localtime(elapsed_time)

    # Format the elapsed time using strftime
    elapsed_time_formatted = time.strftime("%M:%S", elapsed_time_tuple)

    
    # Print the elapsed time
    print("Elapsed time:", elapsed_time_formatted)
    
    time.sleep(1)

'''

'''
# Ask the user for the month, day, and year
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
year = int(input("Enter the year (YYYY): "))

# Calculate the number of days between the given date and today's date
days = calc_days(month, day, year)

# Print the number of days
print(f"The number of days between {month}/{day}/{year} and today is {days}.")
'''