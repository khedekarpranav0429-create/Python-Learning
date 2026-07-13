def Get_Factorial(Number):
    Factorial=1
    while Number>1:
        Factorial=Factorial * Number
        Number=Number-1
    return Factorial
print("Factorial Using Faction")
Number1= int(input("Enter the number "))
print(Get_Factorial(Number1))