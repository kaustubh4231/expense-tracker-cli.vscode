#starting details  
while True:
    print("*** Expense Tracker ***")
    print("1.add expenses \n2. view expenses \n3. calculate total\n4. search expenses\n5. exit")


    choice = int(input("Enter your choice: "))

    if choice ==5:
        print("Thank you for using Expense Tracker!")
        break

    elif choice == 1:
        expenses = input("enter your expense name: ")
        amount = int(input("amount spent: "))

        f = open("expenses.txt" , "a")
        f.write(expenses  +","+ str(amount) + "\n" )
        f.close()
        print("expense has been added successfully")

    elif choice == 2:
        f =  open("expenses.txt","r")
        data= f.read()
        print("===YOUR EXPENSES ARE : ",data)
        f.close()

    elif choice == 3:
        f=open("expenses.txt","r")
        data= f.read()
        f.close()

        total = 0

        for line in data.splitlines():
            parts = line.split(",")
            amount = int(parts[1])
            total = total + amount

        print("total expenses",total)

    elif choice == 4:
        search = input("enter expenses to search: ")

        f=open("expenses.txt","r")
        data = f.read()
        f.close()

        found = False

        for line in data.splitlines():
            if search in line:
                print("your",search,"expenses are: " ,line)
                found = True
        if found == False:
            print("no such expenses found: ")


            
