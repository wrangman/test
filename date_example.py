
from datetime import date as Date

def calc_days(month, day, year):
    # Calculate the date object for the given date
    date1 = Date(year, month, day)

    # Calculate the date object for today's date
    date2 = Date.today()

    # Calculate the difference between the two dates in days
    delta = date2 - date1

    # Return the number of days
    return delta.days


# Ask the user for the month, day, and year
month = int(input("Enter the month (1-12): "))
day = int(input("Enter the day (1-31): "))
year = int(input("Enter the year (YYYY): "))

# Calculate the number of days between the given date and today's date
days = calc_days(month, day, year)

# Print the number of days
print(f"The number of days between {month}/{day}/{year} and today is {days}.")
