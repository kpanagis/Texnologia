def date(c):
      
    if c[2] >= 2021 and c[2] <= 2022:
          
        if c[1] != 0 and c[1] <= 12:
              
            if c[1] == 2 and c[0] != 0 and c[0] <= 31:
                  
                if c[2]%4 == 0 and c[0] <= 29:
                    pass
                  
                elif c[0]<29:
                    pass
                  
                else:
                    print("Invalid date\n")
                    username.pop(i)
                    phonenumber.pop(i)
                    add.pop(i)
                    checkin.pop(i)
                    checkout.pop(i)
                    select_parking_spot()
              
              
            # if month is odd & less than equal 
            # to 7th  month 
            elif c[1] <= 7 and c[1]%2 != 0 and c[0] <= 31:
                pass
              
            # if month is even & less than equal to 7th
            # month and not 2nd month
            elif c[1] <= 7 and c[1]%2 == 0 and c[0] <= 30 and c[1] != 2:
                pass
              
            # if month is even & greater than equal 
            # to 8th  month
            elif c[1] >= 8 and c[1]%2 == 0 and c[0] <= 31:
                pass
              
            # if month is odd & greater than equal
            # to 8th  month
            elif c[1]>=8 and c[1]%2!=0 and c[0]<=30:  
                pass
              
            else: 
                print("Invalid date\n")
                username.pop(i)
                phonenumber.pop(i)
                add.pop(i)
                checkin.pop(i)
                checkout.pop(i)
                select_parking_spot()
                  
        else:
            print("Invalid date\n")
            username.pop(i)
            phonenumber.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            select_parking_spot()
              
    else:
        print("Invalid date\n")
        username.pop(i)
        phonenumber.pop(i)
        add.pop(i)
        checkin.pop(i)
        checkout.pop(i)
        select_parking_spot()
   
   
# Booking fucntion 
def select_parking_spot():
      
        # used global keyword to 
        # use global variable 'i'
        global i
        print(" Select Parking Spot")
        print(" ")
          
        while 1:
            n = str(input("Vehicle: "))
            p1 = str(input("Plate No.: "))
            a = str(input("Address: "))
                        
              
            # checks if any field is not empty
            if n!="" and p1!="" and a!="":
                name.append(n)
                add.append(a)
                break
                  
            else:
                 print("\tVehicle, Plate No. & Address cannot be empty..!!")
               
        cii=str(input("Check-In: "))
        checkin.append(cii)
        cii=cii.split('/')
        ci=cii
        ci[0]=int(ci[0])
        ci[1]=int(ci[1])
        ci[2]=int(ci[2])
        date(ci)
           
        coo=str(input("Check-Out: "))
        checkout.append(coo)
        coo=coo.split('/')
        co=coo
        co[0]=int(co[0])
        co[1]=int(co[1])
        co[2]=int(co[2])
          
        # checks if check-out date falls after 
        # check-in date
        if co[1]<ci[1] and co[2]<ci[2]:
              
            print("\n\tEeeeee mpine..!!\n\tCheck-Out date must fall after Check-In\n")
            username.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            select_parking_spot()
        elif co[1]==ci[1] and co[2]>=ci[2] :
              
            print("\n\tEeeeee mpine..!!\n\tCheck-Out date must fall after or the same day with the Check-In\n")
            username.pop(i)
            add.pop(i)
            checkin.pop(i)
            checkout.pop(i)
            select_parking_spot()
        else:
            pass
          
        date(co)
        d1 = datetime.datetime(ci[2],ci[1],ci[0])
        d2 = datetime.datetime(co[2],co[1],co[0])
        d = (d2-d1).days
        day.append(d)
           
        print("----SELECT Spot----")
        print(" 1. Standard Spot")
        print(" 2. Premium Spot")

        print(("\t\tPress Help for Helpdesk"))
          
        ch=int(input("->"))
          
        # if-conditions to display alloted room
        # type and it's price
        if ch==0:
            print(" 1. Standard Spot - Rs 2$")
            print(" 2. Premium Spot - Rs 5$")
           
            ch=int(input("->"))
        if ch==1:
            spot.append('Standard Spot')
            print("Spot Type- Standard ")  
            price.append(5$)
            print("Price- 5$")
        elif ch==2:
            room.append('Premium Spot')
            print("Spot Type- Premium")
            price.append(7$)
            print("Price- 7$")
        else:
            print(" Wrong choice..!!")
   
  
        # randomly generating room no. and customer 
        # id for customer
        sn = random.randrange(40)+300
        uid = random.randrange(40)+10
          
          
        # checks if alloted room no. & customer 
        # id already not alloted
        while sn in spotno or cid in userid:
            sn = random.randrange(60)+300
            uid = random.randrange(60)+10
              
        rc.append(0)
        p.append(0)
                
        if p1 not in phno:
            phonenumber.append(p1)
        elif p1 in phonenumber:
            for n in range(0,i):
                if p1== phonenumber[n]:
                    if p[n]==1:
                        phonenumber.append(p1)
        elif p1 in phonenumber:
            for n in range(0,i):
                if p1== phonenumber[n]:
                    if p[n]==0:
                        print("\tPhone no. already exists and payment yet not done..!!")
                        username.pop(i)
                        add.pop(i)
                        checkin.pop(i)
                        checkout.pop(i)
                        select_parking_spot()
        print("")
        print("\t\t\t***SPOT BOOKED SUCCESSFULLY***\n")
        print("Spot No. - ",sn)
        print("User Id - ",uid)
        spotnumber.append(sn)
        userid.append(uid)
        i=i+1
        n=int(input("0-BACK\n ->"))
        if n==0:
            Home()
        else:
            exit()
