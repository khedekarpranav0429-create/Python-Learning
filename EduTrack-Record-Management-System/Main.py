Student={202:{"Name":"Pranav","Age":22,"Course":"Machine Learning","Marks":10}}
def Operation():
    try:
        print("\n 1.Add Student \n 2.Display Records \n 3.Search Record \n 4.Update Record \n 5.Delete Record \n 6.exit \n")
        Number=int(input("\n How May i Help You \n"))
        return Number
    except:
        print("Invalid Number")
        return 0
def Add_Record():
    while True:
        student_Id=int(input("\n Enter Student Id"))
        Student[student_Id]={"Name":input("\n Enter Name of the Student\n"),"Age":int(input("\n Enter Age of the Student\n")),"Cousrse":input("Enter the Course Of the Student\n"),"Marks":int(input("Enter Marks Of the Student\n"))}       
        print("\nRecord Added Sucessfully")
        Choice=input("\nDo you want to add another Record[yes/no]\n")
        if Choice.lower() == "yes":
            continue
        elif Choice.lower()=="no":
            break
        else:
            print("Invalid Input")
def Display_Record():
    for student,Details in Student.items():
        for key,value in Details.items():
            print(key,value)
    print("Record Display")
def Search_Record():
    print("Record Search")
    Temp_ID=int(input("\nEnter The Student identity number to be Search\n"))
    if Temp_ID in Student:
        print("Record Fount\n")
        print(Student[Temp_ID])
    else:
        print("Record not Found")
def Update_Record():
    while True:
        Update_Id=int(input("\nEnter The Student Id Which Has to Be Updated\n"))
        update_query=int(input("\n Enter What to Update \n 1.Name\n2.Age\n3.Course\n4.Marks\n"))
        if  update_query==1:
            Student[Update_Id]["Name"]=input("\nEnter Name\n")
        elif update_query==2:
            Student[Update_Id]["Age"]=int(input("\nEnter Age\n"))
        elif update_query==3:
            Student[Update_Id]["Course"]=input("\nEnter Course\n")
        elif update_query==4:
            Student[Update_Id]["Marks"]=int(input("\nEnter Marks\n"))
        else:
            print("\nInvalid Number\n")
        print ("\nRecord Updated Successfully\n")
        Choice=input("\nDo you want to Update another Record[yes/no]\n")
        if Choice.lower() == "yes":
            continue
        elif Choice.lower()=="no":
            break
        else:
            print("\nInvalid Input")
def Delete_Record():
    while True:
        Update_Id=int(input("\nEnter The Student Id Which Has to Be Deleted\n"))
        update_query=int(input("\n Enter What to Delete \n 1.Name\n2.Age\n3.Course\n4.Marks\n5.All Data\n"))
        if  update_query==1:
            del Student[Update_Id]["Name"]
        elif update_query==2:
            del Student[Update_Id]["Age"]
        elif update_query==3:
            del Student[Update_Id]["Course"]
        elif update_query==4:
            del Student[Update_Id]["Marks"]
        elif update_query==5:
            del Student[Update_Id]
        else:
            print("\nInvalid Number\n")
        print ("\nRecord Deleted Successfully\n")
        Choice=input("\nDo you want to delete another Record[yes/no]\n")
        if Choice.lower() == "yes":
            continue
        elif Choice.lower()=="no":
            break
        else:
            print("\nInvalid Input")   
    print("Record Deleted")
def Loop():
    while True:
         Get_operation=Operation()
         if Get_operation > 6:
             print("invalid Number, Choose From the given One")
         elif Get_operation == 1:
             print("\n Add Record")
             Add_Record()
         elif Get_operation == 2:
             print("\n Display Record")
             Display_Record()
         elif Get_operation == 3:
             print("\n Search Record")
             Search_Record()
         elif Get_operation == 4:
             print(" Update Record")
             Update_Record()
         elif Get_operation == 5:
            print("Delete Record")
            Delete_Record()
         elif Get_operation == 6:
            print("Thank You")
            break
         else:
            exit
print("Student Management System")
Loop()


    








