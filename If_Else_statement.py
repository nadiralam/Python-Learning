# email = input("enter the email:- ")
# password = input("enter the password:- ")

# if email=="campusx@gmail.com" and password=="1234":
#    print("welcome")
# elif  email=="campusx@gmail.com" and password !="1234":
#      print("password is incorrect")
#      password =  input("enter the password again:-")
#      if password == "1234":
#          print("Finally correct")
#      else:
#          print(" Still wrong password")    
# else:
#    print("informations are wrong") 


email = input("enter the email:- ")
if '@'in email:
    password = input("enter the password:- ")

    if email=="campusx@gmail.com" and password=="1234":
       print("welcome")
    elif  email=="campusx@gmail.com" and password !="1234":
         print("password is incorrect")
         password =  input("enter the password again:-")
         if password == "1234":
           print("Finally correct")
         else:
           print(" Still wrong password")    
    else:
        print("informations are wrong") 

else:
    print("Email glat hai sahi likho")