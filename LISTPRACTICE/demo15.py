temps=[30,36,40,33,37,29,38]
count=0
for t in temps:
    if t>35:
        count+=1
print("Hot days:",count)