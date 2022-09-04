n=int(input("Enter year:"))
if n%400==0:
    print("leap year")
elif n%100==0:
    print("non leap year")
elif n%4==0:
    print("leap year")
else:
    print("non leap year")