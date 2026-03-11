books=[]
while True:
    print("--Library---")
    print("1:AddBooks\n2:ShowBooks\n3:UpdateBooks\n4:DeleteBook\n5:Exit")
    choice=int(input("Enter choice number:"))
    if choice==1:
        title=input("Enter books title:").lower()
        if title not in books:
            books.append(title)
            print(f"{title} Book added succesfully!")
        else:
            print(f"{title} Book already exist so add another book")
    elif choice==2:
        if len(books)==0:
            print("No books available try again")
        else:
            print("Available books are:",books)
    elif choice==3:
        pass
    elif choice==4:
        pass
    elif choice==5:
        print("Thank you for using our services!!")
        break