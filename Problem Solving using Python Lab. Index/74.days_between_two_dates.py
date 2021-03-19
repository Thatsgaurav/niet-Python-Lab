# WAP to calculate number of days between two dates

from datetime import date
f_date = date(2020, 3, 2)
l_date = date(2021, 3, 11)
delta = l_date - f_date
print(delta.days)