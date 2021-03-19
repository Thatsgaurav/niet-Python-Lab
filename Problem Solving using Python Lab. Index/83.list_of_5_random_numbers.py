# WAP to make a list of 5 random numbers 

import random
res = [random.randrange(1, 50, 1) for i in range(5)]
print ("Random number list is : " +  str(res))