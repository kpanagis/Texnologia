def choices():
    print("Welcome to SPS")
    choice = int(input("For Sigining Up Type 1 and For Signing in Type 2: "))
    if choice == 1:
       return Signup()
    elif choice == 2:
       return Login()
    else:
       raise TypeError

def Signup():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("users.txt",'r')
    info = f.read()
    if name in info:
        return "Name Unavailable. Please Try Again"
    f.close()
    f = open("users.sql",'w')
    info = info + " " +name + " " + password
    f.write(info)

def Login():
    print("Please Provide")
    name = str(input("Name: "))
    password = str(input("Password: "))
    f = open("users.txt",'r')
    info = f.read()
    info = info.split()
    if name in info:
        index = info.index(name) + 1
        usr_password = info[index]
        if usr_password == password:
            return "Welcome Back, " + name
        else:
            return "Password entered is wrong"
    else:
        return "Name not found. Sign Up."

print(choices())
