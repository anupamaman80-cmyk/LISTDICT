phonebook={}

while True:
    print("1 Add Contact")
    print("2 Show Contact")
    print("3 Search Contact")
    print("4 Delete Contact")
    print("5 Exit")
    
    choice = input("Enter choice:")
    
    if choice=="1":
        name=input("Name: ")
        phone=input("Phone: ")
        phonebook[name]=phone
    elif choice=="2":
        print(phonebook)
    elif choice=="3":
        name=input("Enter name: ")
        print(phonebook.get(name, "Not Found"))
    elif choice=="4":
        name=input("Enter name: ")
        phonebook.pop(name,None)
    elif choice=="5":
        break