# Python program to display your details like name, age, address in three different lines

def personal_details():
    name, age = "Gaurav", 19
    address = "Delhi, India"

    # User Input
    # name = str(input("Enter your name :"))
    # age = int(input("Enter your age :"))
    # address = str(input("Enter your address :"))
    
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()