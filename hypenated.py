name=input("enter a name:")
a=len(name)
for i in range(a):
    print(name[i],end="")
    if(i==a-1):
        print("",end="")
    else:
        print("-",end="")
