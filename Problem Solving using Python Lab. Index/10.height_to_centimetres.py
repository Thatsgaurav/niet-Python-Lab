#  Python program to convert height (in feet and inches) to centimetres.
# (1 feet= 12 inches, 1 inch=2.54 cm)
# (cms=feet*12*2.54+inches*2.54)

print("Input your height: ")
h_ft = int(input("Feet: "))
h_inch = int(input("Inches: "))
 
h_inch += h_ft * 12
h_cm = round(h_inch * 2.54, 1)
 
print("Your height is : %d centimeters." % h_cm)