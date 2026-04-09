menu={
    "Samosa":15,
    "Tea":10,
    "Coffee":20,
    "Burger":40,
    "Sandwich":30,
}
cart=[]

print("Menu:")
for item,price in menu.items():
    print(item,":",price)
    while True:
        item=input("Enter item name to add to cart(type 'done' to stop):")
    if item.lover()=="done":
        break
    if item in menu:
        cart.append(item)
        print("item not available")
    else:
        print("Item not available")
total=0
print("\n---- Receipt -----")

for item in cart:
    price=menu[item]
    print(item,":",price)
    total+=price
print("-----------------")
print("Total Price:",total)
