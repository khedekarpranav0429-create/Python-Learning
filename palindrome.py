def palindrome(Get_Number):
    Sum=""
    for number in str(Get_Number):
        Sum = number+Sum
    if Sum==Get_Number:
        print("The Number is Palindrome")
    else:
        print("The Number is Not Palindrome")
print("This is the Demonstration of For Loop,If Else,and Function Usinf Palindrome Logic")
Number=input("Enter The Number")
palindrome(Number)

