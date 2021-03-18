# Python program to convert all units of time into seconds.
# (s=hrs*3600+mins*60) 

hours = int(input("Input hours: ")) * 3600
minutes = int(input("Input minutes: ")) * 60

second = hours + minutes 

print("The time in seconds is", second)
