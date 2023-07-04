a=input("enter your name:")
l=len(a)
b=""
for i in range(l):
    if(a[i].isalpha()):
        b=b+a[i]
        # print(b)fi
print(b)

a=input("enter your name:")
b=""
for i in a:
    if(i!= " "):
        b+=i
print(b)
