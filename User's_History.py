 def Users_Record():
      
    # checks if any record exists or not
    if phno!=[]:
        print("        *** USER'S RECORD ***\n")
        print("| Name        | Phone No.    | Vehicle       | User's Class  | Check-Out     | Room Type     | Price      |")
        print("----------------------------------------------------------------------------------------------------------------------")
          
        for n in range(0,i):
            print("|",name[n],"\t |",phno[n],"\t|",Vehicle[n],"\t|",Users_Class[n],"\t|",username[n],"\t|",Penalty[n])
          
        print("----------------------------------------------------------------------------------------------------------------------")
      
    else:
        print("No Records Found")
    n = int(input("0-BACK\n ->"))
    if n == 0:
        Home()
          
    else:
        exit()
