a=[4, 5, 67, 6, 3, 78, 67]
even=[]
odd=[]
for i in range(len(a)):
    if(i%2==0):
        even.append(a[i])
    elif(i%2!=0):
        odd.append(a[i])
print(even)
print(odd)