
print("1,addition")
print("2,subtraction")
print("3,multiplication")
print("4,division")
print("5,exit")

a = int(input("enter the operation"))

if a==1:
    num1=int(input("enter the 1st num"))
    num2=int(input("enter the 2nd num"))
    result=num1+num2
    print(result)
elif a==2:
    num1=int(input("enter the 1st num"))
    num2=int(input("enter the 2nd num"))
    result=num1-num2
    print(result)
elif a==3:
    num1=int(input("enter the 1st num"))
    num2=int(input("enter the 2nd num"))
    result=num1*num2
    print(result)
elif a==4:
    num1=int(input("enter the 1st num"))
    num2=int(input("enter the 2nd num"))
    result=num1/num2
    print(result)
elif a>=5:
    print(exit)   