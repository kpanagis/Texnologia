def Main_Page()
menu = {}
menu['1']="Vehicle Selection." 
menu['2']="Manage Profile."
menu['3']="Offers"
menu['4']="Update Situation"
menu['5']="Exit"
while True: 
  options=menu.keys()
  options.sort()
    for entry in options: 
      print entry, menu[entry]

    selection=raw_input("Please Select:") 
    if selection =='1': 
      print "Redirecting to Vehicle Selection" 
    elif selection == '2': 
      print "Redirection to Profile Management"
    elif selection == '3':
      print "Go to Offers" 
       if selection =='4':
        print "Situation Update" 
    elif selection == '5': 
      break
    else: 
      print "Unknown Option Selected!" 
      
