Records=[]

def add_student():
    name=input("Enter Name: ")
    roll_no=input("Enter Roll No: ")
    course=input("Enter Course: ")
    marks=int(input("Enter Marks: "))
    Records.append({"Name":name,"Roll no": roll_no, "Course":course, "Marks":marks})
    print("Record successfully saved")

def display_records():
    if Records:
        for record in Records:
            print(f"Name : {record["Name"]}")
            print(f"Roll No: {record["Roll no"]}")
            print(f"Course: {record["Course"]}")
            print(f"Marks: {record["Marks"]}")
    else:
        print("Record is Empty")

def search_student():
    if Records:
        roll_no=input("Enter Roll no")
        for index, record in enumerate(Records):
           if roll_no==record["Roll no"]:
               return record,index
        return None,None
    else:
        print("Unable to search. Enter Records first")
        return None,None

def update_records():
     found,index= search_student()
     if found:
        print(".......")
        print("Record found")
        print(".......")
        print(f"Name : {found["Name"]}")
        print(f"Roll No : {found["Roll no"]}")
        print(f"Course : {found["Course"]}")
        print(f"Marks : {found["Marks"]}")
        marks=input("Enter Marks to update")
        Records[index]["Marks"]=marks
        print("Marks update succefully")
     else:
        print("unable to found!....Add record first")

def delete_records():
    found,index=search_student()
    if found:
        print(".......")
        print("Record found")
        print(".......")
        print(f"Name : {found["Name"]}")
        print(f"Roll No : {found["Roll no"]}")
        print(f"Course : {found["Course"]}")
        print(f"Marks : {found["Marks"]}")
        Records.remove(found)
        print("Record deleted succesfully")
    else:
        print("Record not found!...Unable to delete")
        
def sort_records():
    if Records:
        Records.sort(key= lambda x:x["Marks"],reverse=True)
        print("Record sucessfully sorted by marks....")
    else:
        print("Records are empty!...Unable to sort")
    
            

#for update records
while True:
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")      
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Student")
    print("7. Exit")

    choice=input("Enter Choice: ")
    if choice=="1":
        #Add Student
        add_student()
        
    elif choice=="2":
        #Display Student
        display_records()
    elif choice=="3":
        #Search Student
        record,index=search_student()
        if record is not None:
            print(f"Name : {record["Name"]}")
            print(f"Roll No: {record["Roll no"]}")
            print(f"Course: {record["Course"]}")
            print(f"Marks: {record["Marks"]}")
        else:
            print("Record not found")
    
    elif choice=="4":
        #Update Student
        update_records()
    elif choice=="5":
        #Delete Student
        delete_records()
    elif choice=="6":
        #Sort Student
        sort_records()
    elif choice=="7":
        #exit
        break
    else:
        print("Invalid choice")
