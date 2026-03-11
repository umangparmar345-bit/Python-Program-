#write a program to createa list and perform various operation on list using manu

lst=[]

while True:
    print("\n-- List Operation")
    print("1.Add Element")
    print("2.Delete Element")
    print("3.Display List")
    print("4.Sorted List")
    print("5.Search Element")
    print("6.Exit")

    choice=int(input("Enter Your Choicer:="))
    if choice==1:
        item=int(input("Enter to Element Add:"))
        lst.append(item)
        print("Element Add")
    elif choice==2:
         item=int(input("Delete Element:-"))
         if item in lst:
             lst.remove(item)
             print("Element Deleted")
         else:
             print("Element Not found")
    elif choice==3:
         item=int(input("Display the List:=",lst))

    elif choice==4:
         lst.sort()
         print("Sorted List",lst)
    elif choice==5:
         item=int(input("Enter element to serach:"))
         if item in lst:
             print("Element found in list")
         else:
              print("Element Not found")
    elif choice==6:
        print("Exiting program. Goodbye!")
        break
    
    else:
        print("Invalid choice! Please try again.")
