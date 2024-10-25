def addservice():
    name1 = ''
    productlist = []
    def checking():
        name1 = input("What's the name of the product? ")
        if name1 in productlist:
            print('Already added.')
        else:
            productlist.append(name1)
            print(f'Done. Added: {productlist}\n')

    def seelist():
        wannaseelist = input("Do you want to see the current products then? y/n\n")
        if wannaseelist == "yes" or wannaseelist == "y":
            print(f"{productlist}")

    keeprunning = input("Do you want to add new products to the list? y/n\n")
    if keeprunning == "no" or keeprunning == "n":
        seelist()
    
    while keeprunning == "y" or keeprunning == "yes":
        checking()
        keeprunning = input("carDo you still want to add new products to the list? y/n\n")
    else:
        print("\nDone.")
        input("Press any key to exit.")

addservice()