# Python Program to Convert Kilometres to Miles (1 mile = 1.67 km)

km = float(input("Enter value in kilometers: "))

# 1km = 0.621371 miles
conv_fac = 0.621371
miles = km * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(km,miles))
