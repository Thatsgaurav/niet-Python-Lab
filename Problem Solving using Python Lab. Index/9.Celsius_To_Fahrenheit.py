# Python Program to Convert Celsius To Fahrenheit
# F=9*C/5+32

celsius = float(input("Enter the celsius value :"))
# celsius = 37.5

# calculate fahrenheit
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))