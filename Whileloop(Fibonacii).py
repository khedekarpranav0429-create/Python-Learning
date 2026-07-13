Get_Number1=int(input("enter first digit"))
Get_Number2=int(input("enter the second Digit"))
Limit=int(input("Enter the n Value"))
Count=1
print(Get_Number1)
print(Get_Number2)
while Count<= Limit-2:
    Sum=Get_Number1+Get_Number2
    print(Sum)
    Get_Number1=Get_Number2
    Get_Number2=Sum
    Count=Count+1
