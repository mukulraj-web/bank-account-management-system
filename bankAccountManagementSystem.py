def ams():
    
    userDb = {}
    while True:
          command = int(input("what do you want from bank dial(1: for register,2: for enquiry,3: for quit,4: for change detail, 5: for deposit and 6: for withdrwal): "))
          if command == 1:
              
              userData = {}
              name = input("enter your name: ")
              
              keys = {"name","account_num","mobile_num","opening_balance","address","pincode","age"}
              for key in keys:
                  value = input(f"enter you {key}:")
                  userData[key] = value
                  userDb[name] = userData

                  print(f"Registration successful for {name}.")
          elif command == 2:
            name = input("enter the name for enquiry and security purpose: ")
            if name in userDb:
                queary = str(input("enter your queary like (account detail,balance): "))
            else:
                print(f"{name} is not registered")
            if queary == "balance":
                print("balance: ",userDb[name].get("opening_balance"))
                continue
            elif queary == "account detail":
                print(f"Acccount detail from {name}: ", userDb[name])
                continue
          elif command == 3:
            
            print("good bye")
            break
          elif command == 5:
             name = input("enter your name: ")
             if name in userDb:
                deposit = float(input("enter amount to deposite and dont forget to give money: "))
                openingBal=float((userDb[name]["opening_balance"]))
                openingBal+=deposit
                userDb[name]["opening_balance"] = openingBal
                print("Deposit sucessful of amount",deposit)
                print("your balance is: ",userDb[name]["opening_balance"])
          elif command == 6:
              name = input("enter your name: ")
              if name in userDb:
                  withdrawingAmount = float(input("enter amount to withdraw: "))
                  openingBal = float(userDb[name]["opening_balance"])
                  openingBal-=withdrawingAmount
                  print("withdraw sucessfull of amount",withdrawingAmount)
                  userDb[name]["opening_balance"] =openingBal
                  print("closing_balance: ", openingBal)
                  
                 
          elif command == 4:
             name = input("enter your name: ")
             if name in userDb:
                 print("ok wait we are fetching your data")
                 objectToChange = str(input("what do you want to change in details (name,mobile_number,address,pincode,age): ")).lower()
                 if  objectToChange == "name":
                     name = input("enter you name registered to bank: ")
                     newName = input("enter a new name: ")
                     userName=userdb[name]["name"]#i stuck on change name next day i will start from changing number#
                     print(userName)
                     print(newName)
                     print(userDb[name])
        
                    
                 
             
          else:
            print("invalid command")
        


ams()   

        
        
           
        
    










    

