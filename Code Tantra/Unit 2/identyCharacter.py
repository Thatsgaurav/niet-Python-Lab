# WAP to enter a character and then determine whether it is a vowel, consonants, or a digit.

ch = input("Enter a alphabet or digit ")

if ch == '0' or ch == '1' or ch == '2' or ch == '3' or ch == '4' or ch == '5' or ch == '6' or ch == '7' or ch == '8' or ch == '9':
    print(ch, "is a digit.")
elif ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U':
    print(ch, "is a vowel.")
else:
    print(ch, "is a consonant.")
