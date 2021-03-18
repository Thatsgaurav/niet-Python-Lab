# Python program to compute the distance between the points (x1, y1) and (x2, y2)

import math
p1 = []
p2 = []
p1.append(int(input("Enter x1 = ")))
p1.append(int(input("Enter y1 = ")))
p2.append(int(input("Enter x2 = ")))
p2.append(int(input("Enter y2 = ")))
print(p1)
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)