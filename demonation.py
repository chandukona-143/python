amount=int(input("enter a amoumt:"))
five_hundreds=amount//500
remaining_balance=amount%500
hundreds=remaining_balance//100
remaining_balance2=remaining_balance%100
fifties=remaining_balance2//50
remaining_balance3=remaining_balance2%50
tens=remaining_balance3//10
remaining_balance4=remaining_balance3%10

print("Five Hundred notes(500) : ",five_hundreds)
print("Hundred notes(100):",hundreds)
print("fifty rupees notes(50):",fifties)
print("ten rupes(10):",tens)
