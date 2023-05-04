import datetime

# Get the current date and time
now = datetime.datetime.now()

# Print the current date and time in various formats
print("Current date and time:", now)
print("Current year:", now.year)
print("Current month:", now.month)
print("Current day:", now.day)
print("Current hour:", now.hour)
print("Current minute:", now.minute)
print("Current second:", now.second)

# Create a datetime object representing a specific date and time
dt = datetime.datetime(2022, 1, 1, 12, 0, 0)

# Calculate the difference between two datetimes
diff = dt - now
days = diff.days
hours = diff.seconds // 3600
minutes = (diff.seconds // 60) % 60

# Print the time until the specified datetime
print("Time until Jan 1, 2022, 12:00 PM:", days, "days,", hours, "hours,", minutes, "minutes")
