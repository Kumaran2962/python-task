x=[[1,2,3],[4,5,6],[7,8,9]]
y=[[1,2,3],[4,5,6],[7,8,9]]
print("3*3 x matrix")
for i in range(3):
    for j in range(3):
        print(x[i][j],end=" ")
    print()
print()    
print("3*3 y matrix")
for i in range(3):
    for j in range(3):
        print(y[i][j],end=" ")
    print()
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(len(x[0])):
        result[i][j]=x[i][j]+y[i][j]
print()
print("resultant matrix")
for i in range(3):
    for j in range(3):
        print(result[i][j],end=" ")
    print()

