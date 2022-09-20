num=int(input())
num1=int(input())
a=0
for i in range (num,num1):
    if(num%i)==0:
        a=0
        print("not prime")
        break
    else:
        a=1
    if a==1:
        print("prime number")