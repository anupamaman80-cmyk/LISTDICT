ages=[5,12,18,25,40,15]
minor=[]
adult=[]
for age in ages:
    if age<18:
        minor.append(age)
    else:
        adult.append(age)
print("Minors:",minor)
print("Adults:",adult)