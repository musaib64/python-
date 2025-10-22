
dict1={}
count =0
while True:

    name=input("enter the student name :")
    roll=int(input("enter the roll numeber :"))
    sem=input("enter the semester : ")
    #storing data in dictionary and removing duplicates
    if roll not in dict1:
        dict1[roll]={"student name":name,"sem":sem}
    else:
        print("Student with roll number", roll, "already exists.")
    count +=1
    #modify option to add more student details
    
    ch=input("do you want to add more student details y/n :")
    if ch.lower()=='n':
        break

for j in dict1:
    n=int(input("enter the roll number to get student details :"))
    if n in dict1:
        print(f"student name :{dict1[n]['student name']}\nsemester :{dict1[n]['sem']}")
        print("number of students is ", count)
        break
    else:
        print("roll number not found")
        


