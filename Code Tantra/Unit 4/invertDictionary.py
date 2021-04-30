# WAP that inverts a dictionary. That is, it makes key of one dictionary value of another and vice versa.

l1 = input("Enter elements separated by ,(comma) for keys: ").split(",")
l2 = input("Enter elements separated by ,(comma) for values: ").split(",")
d1 = {}
d2 = {}
if len(l1) == len(l2):
    for i in range(len(l1)):
        d1[l1[i]] = l2[i]
        d2[l2[i]] = l1[i]
print("Dict :", d1)
print("Inverted Dict :", d2)
