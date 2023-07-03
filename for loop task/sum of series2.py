a=int(input("enter the number of terms: "))
t=9
sum=1
for i in range(a+1):
    sum+=t
    print(t)
    t=t*10+9
print("the sum of the series: ",sum)