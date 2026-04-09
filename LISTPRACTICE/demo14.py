prices=[100,200,150,300,250]
total=0
for price in prices:
    total+=price
avg=total/len(prices)
print("Total bill:,total")
print("Average price:",avg)