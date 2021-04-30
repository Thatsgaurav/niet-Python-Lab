# Python program to convert all units of time into seconds.
# (s=day*24*3600+hrs*3600+mins*60)

days = int(input("Enter number of days ")) * 3600 * 24
hours = int(input("Enter time in hours ")) * 3600
minutes = int(input("Enter time in minutes ")) * 60
units = days + hours + minutes
print("Time in seconds =", units)
