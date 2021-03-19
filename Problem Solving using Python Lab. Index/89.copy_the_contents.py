# WAP to copy the contents of one file into another file

with open('first.txt','r') as firstfile, open('second.txt','a') as secondfile: 
    for line in firstfile: 
             secondfile.write(line)