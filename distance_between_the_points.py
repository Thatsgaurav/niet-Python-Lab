# Python program to compute the distance between the points (x1, y1) and (x2, y2).

import math
p1 = []
p2 = []
p1.append(int(input("Enter First x = ")))
p1.append(int(input("Enter First y = ")))
p2.append(int(input("Enter Second x = ")))
p2.append(int(input("Enter Second y = ")))
print(p1)
distance = math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )

print(distance)