# Python program to calculate number of days between two dates. 

from datetime import date
f_date = date(2021, 1, 24)
l_date = date(2021, 1, 26)
delta = l_date - f_date
print(delta.days)