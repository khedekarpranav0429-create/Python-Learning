Student_Data=[[2039,"Pranav",98,78,69],[1023,"Nidhi",78,67,87],[2052,"Rohan",68,98,75],[2067,"Harshita",97,46,21]]

def Menu():
    while True:
        try:
            print("\n Student Marks Analyzer\n")
            print("----------------------------")
            Choice=int(input("\n1.Add Student Record\n2.View Student Data\n3.Search Student Data\n4.Update Student Data\n5.Delete Student data\n6.Statistic\n7.Exit\n-------------------------------\n\n"))
            
            return Choice
        except:
            print("\nEnter Valid Number\n")

def Loop():
    while True:
        Get_Choice=Menu()
        if Get_Choice < 1 or Get_Choice > 7:
            print("invalid Number")
        elif Get_Choice==1: 
            Add_record()
        elif Get_Choice==2:
            View_Data()
        elif Get_Choice==3:
            Search_Data()
        elif Get_Choice==4:
            Update_Data()
        elif Get_Choice==5:
            Delete_Data()
        elif Get_Choice==6:
            Statistic()
        elif Get_Choice==7:
            break
        else:
            exit
    
def Add_record():
    print("\nAdd Student\n")
    while True:
        RollNumber=int(input("\nEnter Roll Number:\n"))
        Name=input("\n Enter Student Name\n")
        Python=int(input("\n Enter Marks of Python the Student\n"))
        Java=int(input("\n Enter Marks of Java the Student\n"))
        C_Language=int(input("\n Enter Marks C++ of the Student\n"))
        Student=[RollNumber,Name,Python,Java,C_Language]
        Student_Data.append(Student)
        choice=input("\n Do You Want To Save Another Record [Yes/No]\n")
        if choice.lower()=='yes':
            continue
        elif choice.lower()=='no':
            return
            
def View_Data():
    print("\nRecord\n")
    for Record in Student_Data:
        print("\n Roll Number :",Record[0])
        print("\n Name :",Record[1])
        print("\n Python :",Record[2])
        print("\n Java : " ,Record[3])
        print("\n C++ : ",Record[4])

        print("\n-------------------\n") 

def Search_Data():
    print("\nSearch Record\n")
    Get_Data=int(input("\nEnter The Roll Number to Find data\n"))
    for  Record in Student_Data:
        if Record[0]==Get_Data:
            print("\nRecord Found Successfully\n")
            break
        
def Update_Data():
    print("\nUpdate Record\n")
    Get_Data=int(input("\nEnter The Roll Number to Update data\n"))
    while True:
        for i in range(len(Student_Data)):
            if Student_Data[i][0]==Get_Data:
                Get=int(input("\n What You Have To Update\n1.Name\n2.Marks\n"))
                if Get==1 :
                    Student_Data[i][1]=input("\nEnter The Name To Be Updated \n")
                elif Get==2:
                    Student_Data[i][2]=input("\nEnter The Python  To Be Updated \n")
                    Student_Data[i][3]=input("\nEnter The Java To Be Updated \n")
                    Student_Data[i][4]=input("\nEnter The C++ To Be Updated \n")
            
        choice=input("\n Do You Want To Update Another Record [Yes/No]\n")
        if choice.lower()=='yes':
            continue
        elif choice.lower()=='no':
            return

def Delete_Data():
    print("\nDelete Record\n")
    Get_Data=int(input("\nEnter The Roll Number to Delete data\n"))
    for i in range(len(Student_Data)):
        if Student_Data[i][0]==Get_Data:
            del Student_Data[i]
            print("Record Deleted")
            break             

def Statistic():
    print("\nPerformance Data\n")
    Get_Data=int(input("Enter The Roll Number to Student to Check Performance \n"))
    total=0
    avg=0
    min=0
    max=0
    for i in Student_Data:
        marks=i[2:]
        if i[0]==Get_Data:
            min=i[2]
            for j in marks:
                total=total+j
                avg=total/ len(marks)
                
                if j > max:
                    max=j
                if j < min:
                    min=j
    print("\n Total: ",total)
    print("\n Average: ",avg)
    print("\n Maximum: ",max)
    print("\n Minimum: ",min)

Loop()