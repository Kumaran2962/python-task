a=[4, 5, 67, 0, 3, 78, 67]
addition=0
multiplication=1
for i in range (len(a)):
    if a[i]!=0:
        addition=addition+a[i]
        multiplication=multiplication*a[i]
    else:
        continue
    
print(addition)
print(multiplication)