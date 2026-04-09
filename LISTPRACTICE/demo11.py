nums=[-5,3,-2,8]
new_list=[]
for n in nums:
    if n <0:
        new_list.append(-n)
    else:
        new_list.append(n)
print(new_list)