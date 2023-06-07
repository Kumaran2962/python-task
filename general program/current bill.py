unit=float(input("enter the unit comsumed: "))
if(unit<=100):
    print("it is free for below 100 units")
elif(unit <= 200):
    amt=(unit-100)*5
    print("you want to pay",amt)
elif(unit>=201):
    amt=500+(unit-200)*10
    print("you want to pay",amt)
else:
    print("enter a valid number")
# billamt=amt
# print("the Electricity bill is:",billamt)