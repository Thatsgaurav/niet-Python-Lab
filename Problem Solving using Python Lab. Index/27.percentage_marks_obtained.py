#  WAP that accepts the marks of 5 subjects and finds the percentage marks obtained by
# the student. It also prints grades according to the following criteria:
# Between 90-100%-----------Print 'A'
# 80-90%------------------------Print 'B'
# 60-80%------------------------Print 'C'
# 50-60%------------------------Print 'D'
# 40-50%------------------------Print 'E'
# Below 40%-------------------Print 'F’


print("\t Enter the marks of 5 subjects")
p,c,m,e,h = float(input("physics :")),float(input("chemistry :")),float(input("math :")),float(input("english :")),float(input("history :"))
total = p+c+m+e+h
percent = (total*100)/500
print("You have gotten",percent,"%")
if percent >= 90:
    print("Grade A")
elif percent >= 80 and percent < 90:
    print("Grade B")
elif percent >= 70 and percent < 80:
    print("Grade C")
elif percent >= 60 and percent < 70:
    print("Grade D")
elif percent >= 50 and percent < 60:
    print("Grade E")
elif percent >= 40 and percent < 50:
    print("Grade F")
else:
    print("Invalid Input")
    exit()                        