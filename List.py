#write a program to createa list and perform various operation on list using manu



my_list = []

while True:
    print("\n--- LIST OPERATIONS MENU ---")
    print("1. Add element")
    print("2. Insert element at position")
    print("3. Delete element")
    print("4. Display list")
    print("5. Sort list")
    print("6. Search element")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        element = input("Enter element to add: ")
        my_list.append(element)
        print("Element added successfully.")

    elif choice == 2:
        element = input("Enter element to insert: ")
        position = int(input("Enter position: "))
        my_list.insert(position, element)
        print("Element inserted successfully.")

    elif choice == 3:
        element = input("Enter element to delete: ")
        if element in my_list:
            my_list.remove(element)
            print("Element deleted successfully.")
        else:
            print("Element not found.")

    elif choice == 4:
        print("Current List:", my_list)

    elif choice == 5:
        my_list.sort()
        print("List sorted successfully.")

    elif choice == 6:
        element = input("Enter element to search: ")
        if element in my_list:
            print("Element found at index:", my_list.index(element))
        else:
            print("Element not found.")

    elif choice == 7:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
