a =list(input())
for i in range(len(a)):
    if a[i]=='a':
        a[i]='&'
    elif a[i]=='b':
        a[i]='|'
    elif a[i]=='c':
        a[i]='^'    
res = ''.join(a) 
print(eval(res)) 
