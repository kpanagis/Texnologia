print "Login Script"

import getpass

Username = "edwmakris"
Password = "Skrrr" 

loop = 'true'
while (loop == 'true'):

    username = raw_input("Username: ")

    if (username == Username):
        loop1 = 'true'
        while (loop1 == 'true'):
            password = getpass.getpass("Password: ")
            if (password == Password):
                print "Logged in successfully as " + username
		print "Welcome to SPS"
		KALO THN KLASH
                loop = 'false'
                loop1 = 'false'
            else:
                print "Password incorrect!"

    else:
        print "Username incorrect!"
