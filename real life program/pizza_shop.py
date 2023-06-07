# program for pizza shop
print("welcome to pizzahut")
a1="panner"
a2="mushroom"
choice=input("enter your choice:")
if(choice==a1):
    print("you choose panner:")
    b1="onion"
    b2="tomato"
    b3="capsicum"
    choice2=input("enter your topping choices(onion/tomato/capsicum):")
    if(choice2==b1):
        print("you added onion")
    elif(choice2==b2):
        print("you added tomato")
    elif(choice2==b3):
        print("you added capsicum")
    c1="mozzarella"
    c2="cheddar"
    choice3=input("enter you cheese choices(mozzarella/cheddar):")
    if(choice3==c1):
         print("you added Mozzarella cheese")
    elif(choice3==c2):
            print("you added CHEDDAR cheese")
    print("your order is confirmed!!")
elif(choice==a2):
    print("you choose mushroom:")
    b1="onion"
    b2="tomato"
    b3="corn"
    choice2=input("enter your topping choices(onion/tomato/corn):")
    if(choice2==b1):
        print("you added onion")
    elif(choice2==b2):
        print("you added tomato")
    elif(choice2==b3):
        print("you added corn")
    c1="mozzarella"
    c2="cheddar"
    choice3=input("enter you cheese choices(mozzarella/cheddar):")
    if(choice3==c1):
        print("you added Mozzarella cheese")
    elif(choice3==c2):
        print("you added CHEDDAR cheese")
    print("your order is confirmed!!")
else:
    print("thank you!! and visit again")

        
