Phonebook={}

while True:
    print("\n----Phonebook Menu----")
    print("1. Add New Contact")
    print("2. Search for contact")
    print("3. Delete contact")
    print("4. List All contact")
    print("5. Exit")

    choice=input("enter a no between 1-5\n")
    if choice =='1':
        name=input("enter your name:\n")
        if name in Phonebook:
            print("name is already exist")
        else:
            Number=input("enter the number\n")
            Phonebook[name]=Number
            print(f"Contact {name} added successfully")

    elif choice == '2':
        name=input("\nEnter the name to search")
        if name in Phonebook:
            print(f"{name}'s phonenumber is {Phonebook[name]}")
        else:
            print("contact is not found")
    elif choice == '3':
        name=input("enter the name to del\n") 
        if name in Phonebook:
            del Phonebook[name]
        else:
            print("name is not found")
    elif choice == '4':
        if Phonebook:   
            print("\n---List of all phonebook contacts---")
            for name , Number in Phonebook.items():
                print(f"{name}:{Number}")
        else:
            print("Phonebook is empty")  


    elif choice == '5':
        print("Exiting Phonebook! Good Bye")
        break
    else:
        print("Invalid choice please choose correct choice.")      




            