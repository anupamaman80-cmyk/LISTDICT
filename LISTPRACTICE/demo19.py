attendance=[1,1,0,1,0,1,1]
present=attendance.count(1)
absent=attendance.count(0)
percentage=(present/len(attendance))*100
print("Present:",present)
print("Absent:",absent)
print("Attendance %:", percentage)
attendance=[1,1,0,1,0,1,1]
present=0
absent=0
for a in attendance:
    if a==1:
        present+=1
    else:
        absent+=1
percentage=(present/len(attendance))*100

print("Present:",present)
print("Absent:",absent)
print("Attendance %:", percentage)

