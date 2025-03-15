password = input("Enter password:")
spec = ["%","@","_","#","!","?","₹",":",",",".","{","}",";","-","+","|"]
a=b=c=d=False
if len(password) > 7:
    for i in range(len(password)):
        if password[i].isupper():
            a = True
        elif password[i].islower():
            b = True
        elif password[i].isdigit():
            c = True
        elif password[i] in spec:
            d = True

if a and b and c and d:
    print("Valid password")
else:
    print("Invalid password")
