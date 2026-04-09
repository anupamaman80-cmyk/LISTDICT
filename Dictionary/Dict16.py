phonebook={}
while True:
    name=input("Enter name:")
    if name=="exit":
        break
    phone=input("Enter phone number:")
    phonebook[name]=phone
print(phonebook)