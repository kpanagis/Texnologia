import time
import re

password=''
password2=''
def validate_password(password):
      if len(password) <8:
            print 'returning 1'
            return 1
      if not re.search('[0-9]',password):
            return 2
      if not re.search('[a-z]',password):
            return 3
      if not re.search('[A-Z]',password):
            return 4
      return 0

def check_password(password,password2):
      if password==password2:
            return True
      else:
            return False

def get_password():
      password=raw_input('Enter password:')
      flag=validate_password(password)
      if flag==0:
            password2=raw_input('Re-Enter Password:')
            flag2=check_password(password,password2)
            if flag2==True:
                  return True
            else:
                  print 'Passwords do not match!!'
                  return False
      elif flag==1:
            print 'Password must be of 8 characters'
            return False
      elif flag==2:
            print 'Password must contain a number'
            return False
      elif flag==3:
            print 'Password must include a small letter'
            return False
      elif flag==4:
            print 'Password must also include a capital letter'
            return False
def logged():
      print 'Logging in...'
      time.sleep(5)
      print 'Successfully logged in'

def main():
      flag=get_password()
      if flag==True:
            logged()
      else:
            while True:
##                  print ''
                  get_password()
                  
def change_username()
username=''
username2=''
def validate_username(username):
      if len(username) <6:
            print 'returning 1'
            return 1
      if not re.search('[0-9]',username):
            return 2
      if not re.search('[a-z]',username):
            return 3
      if not re.search('[A-Z]',username):
            return 4
      return 0

def check_username(username,username2):
      if username==username2:
            return True
      else:
            return False
            
 
def get_username():
      username=raw_input('Enter username:')
      flag=validate_username(username)
      if flag==0:
            username2=raw_input('Re-Enter Username:')
            flag2=check_username(username,username2)
            if flag2==True:
                  return True
            else:
                  print 'Usernames do not match!!'
                  return False
      elif flag==1:
            print 'Username must be of 6 characters'
            return False
      elif flag==2:
            print 'Username must contain a number'
            return False
      elif flag==3:
            print 'Username must include a small letter'
            return False
      elif flag==4:
            print 'Username must also include a capital letter'
            return False

def change_phone_num
phone_num=''
phone_num2=''
def validate_phone_num(phone_num):
      if  re.search('[0-9]',phone_num):
            return 1
      return 0

def check_phone_num(phone_num,phone_num2):
      if phone_num==phone_num2:
            return True
      else:
            return False
            
def get_phone_num():
      phone_num=raw_input('Enter phone number:')
      flag=validate_phone_num(phone_num)
      if flag==0:
            phone_num2=raw_input('Re-Enter phone number:')
            flag2=check_phone_num(phone_num,phone_num2)
            if flag2==True:
                  return True
            else:
                  print 'Phone numbers do not match!!'
                  return False
      elif flag==1:
            print 'Username must be of 10 numbers'
            return False
    
