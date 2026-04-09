runs=[45,0,10,80,55,90]
count=0
for run in runs:
    if run>50:
        count+=1
print("Matches above 50 runs:", count)
        