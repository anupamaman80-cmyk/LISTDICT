students={}
for i in range(3):
    name=input("Enter student name:")
    marks=int(input("Enter marks:"))
    students[name]=marks
print("All students:", students)
topper=max(students,key=students.get)
print("Topper:", topper)

average=sum(students.values()) / len(students)
print("Average marks:", average)