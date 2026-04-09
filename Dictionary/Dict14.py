inventory={
    "Pens": 10,
    "Erasers": 5
}
item=input("Enter item to buy:")
if item in inventory:
    inventory[item]-=1
    print("Updated inventory:", inventory)
else:
    print("Item not found")
