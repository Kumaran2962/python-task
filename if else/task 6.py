a=int(input("enter the year: "))
if (a%4==0 and a%100!=0 or a%400==0):
    print("the given year is leap year")
else:
    print("the given year is non leap year")    