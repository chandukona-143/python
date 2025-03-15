a = int(input())
op = input()
b  = int(input())
if op == '+':
    print(sum(a,b))
elif op == '-':
    print(a-b)
elif op == '/':
    print(a/b)
elif op == '*':
    print(a*b)
elif op == '//':
    print(a//b)
elif op == '**':
    print(a**b)
else:
    print("Invalid Operator")
