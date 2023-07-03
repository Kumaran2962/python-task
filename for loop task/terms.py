a=int(input("enter the number of terms:"))
s=0.0
for i in range(1,a+1):
    if(i<a):
        print(f"1/{i}")
        s+=1/i
    elif(i==a):
        print(f"1/{i}")
        s+=1/i
print(f"sum of the series upto {a} terms: ",s)