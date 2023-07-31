def swaping():
    a=[1,3,5,7]
    a[0],a[-1]=a[-1],a[0]
    print(a)

def swaping_position():
    a=[12,34,56,78]
    b=int(input("enter the pos1= "))
    c=int(input("enter the pos2= "))
    a[b-1],a[c-1]=a[c-1],a[b-1]
    print(a)

def finding_length():
    a=[23,45,67,89,13,24,35,46,57,68,79]
    b=0
    for i in a:
        b+=1
    print(b)

def verification():
    a=[11,22,33,44,55,66,77,88,99]
    b=int(input("enter the number to be verified: "))
    if b in a:
        print("true")
    else:
        print("false")