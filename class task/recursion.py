n=0
def recursion(a):
    global n
    if(n!=a):
        n+=1
        print(n)
        recursion(a)
recursion(10)