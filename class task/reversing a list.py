a=[4, 5, 67, 6, 3, 78, 67]
b=[]
for i in a:
    b.insert(0,i)
    print(b)
print(b)



a=[4, 5, 67, 6, 3, 78, 67]
b=[]
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)