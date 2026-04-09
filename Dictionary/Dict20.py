attendence={}
for i in range(5):
    name=input("Student name: ")
    status=input("Present or Absent:")
    attendence[name]=status
present=0
absent=[]
for name,status in attendence.items():
    if status=="Present":
        present+=1
    else:
        absent.append(name)
print("Total present:",present)
print("Absent student:",absent)