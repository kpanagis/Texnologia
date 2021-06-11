def Payment():
      
    ph=str(input("Phone Number: "))
    global i
    f=0
      
    for n in range(0,i):
        if ph==phno[n] :
              
            
             if p[n]==0:
                f=1
                print(" Submit and Pay")
                print(" --------------------------------")
                print("  MODE OF PAYMENT")
                   
                print("  Name- Last Name, Surname")
                print("  Telephone- 6969696969")
                print("  Spot Selected- X")
                print("  Reservation Time- From a to b")
                print("  Offers- Chosen Offer")
                print("  Selected Vehicle- Car Y")
                x=int(input("-> "))
                print("\n  Amount: ",(price[n]*hour[n])+rc[n])
                print("\n            Pay For Spot")
                print("  (y/n)")
                ch=str(input("->"))
                  
                if ch=='y' or ch=='Y':
                    print("\n\n --------------------------------")
                    print("           Pay for Spot")
                    print(" --------------------------------")
                    print(" Name: ",name[n],"\t\n Telephone No.: ",phno[n],"\t\n Spot Selected: ",add[n],"\t")
                    print("\n Check-In: ",checkin[n],"\t\n Check-Out: ",checkout[n],"\t")
                    print("\n Selected Vehicle: ",vehicle[n],"\t\n Sum: ",price[n]*hour[n],"\t")
                    print("\n Total Amount: ",(price[n]*hour[n])+rc[n],"\t")
                    print(" --------------------------------")
                    print("Thank You")
                    print("Let's go to your Reservation :)")
                    print(" --------------------------------\n")
                    p.pop(n)
                    p.insert(n,1)
                      
                   
                    roomno.pop(n)
                    custid.pop(n)
                    roomno.insert(n,0)
                    custid.insert(n,0)
                      
             else:
                  
                for j in range(n+1,i):
                    if ph==phno[j] :
                        if p[j]==0:
                            pass
                          
                        else:
                            f=1
                            print("\n\tPayment has been Made :)\n\n") 
    if f==0:    
        print("Invalid Customer Id")
          
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
    else:
        exit()
