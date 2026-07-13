Surnames=["khedekar","Sharma","Kholi","Dhoni"]
print("list of privous Data of Surname")
print(Surnames)
Get_data=input("do you want to add another record")
if Get_data.lower()=='yes':
    New_data=input("Enter The Surname to Be add")
    Surnames.append(New_data)
    fetch=input("do you want to see the Updated data")
    if fetch.lower()=='yes':
        print(Surnames)
    else:
        exit
else:
    exec


