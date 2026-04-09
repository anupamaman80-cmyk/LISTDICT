items={
    "Pen": 10,
    "Notebook":50,
    "Bag":500,
    "Pencil":5
}
cheapest= min(items,key=items.get)
print("Cheapest item:", cheapest)