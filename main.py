import os 
import pyfiglet
import time

#username
print(pyfiglet.figlet_format("Auto Dox"))
username = input('Enter the Username > ')
os.system("cls")

#Last Name
print(pyfiglet.figlet_format("Auto Dox"))
lastName = input('Enter the Last name > ')
os.system("cls")

#First name
print(pyfiglet.figlet_format("Auto Dox"))
firstName = input('Enter the First name > ')
os.system("cls")

#Date of birth
print(pyfiglet.figlet_format("Auto Dox"))
dob = input('Enter the Date of birth > ')
os.system("cls")

#Age
print(pyfiglet.figlet_format("Auto Dox"))
age = input('Enter the Age > ')
os.system("cls")

#City
print(pyfiglet.figlet_format("Auto Dox"))
city = input('Enter the City > ')
os.system("cls")

#Department 
print(pyfiglet.figlet_format("Auto Dox"))
department = input('Enter the Department > ')
os.system("cls")

#Street  
print(pyfiglet.figlet_format("Auto Dox"))
street = input('Enter the Street > ')
os.system("cls")

#Phone Number  
print(pyfiglet.figlet_format("Auto Dox"))
phoneNumber = input('Enter the Phone Number > ')
os.system("cls")

#IP  
print(pyfiglet.figlet_format("Auto Dox"))
ip = input('Enter the IP > ')
os.system("cls")

#Pictures of HIM  
print(pyfiglet.figlet_format("Auto Dox"))
pictureLink = input('Enter the Pictures of HIM (Link) > ')
os.system("cls")

# Reason for DOX
print(pyfiglet.figlet_format("Auto Dox"))
reason = input('Enter the Reason for DOX) > ')
os.system("cls")

# Create by ... 
print(pyfiglet.figlet_format("Auto Dox"))
author = input('Enter the author > ')
os.system("cls") 

print("Creating the dox...")
time.sleep(5)
os.system("cls")
print("Loading the dox...")
time.sleep(3)
os.system("cls")
print("Dox created !")

f = open(f"dox-{username}.txt", "a")
f.write(f"""

Auto Dox By Skl'Dev

Username > {username}
Last Name > {lastName}
First Name > {firstName}
Date of Birth > {dob}
Age > {age}
City > {age}
Department > {department}
street > {street}
Phone Number > {phoneNumber}
IP > {ip}
Picture Link > {pictureLink} :                                                                                                                                   		                
Reason for the Dox > {reason}                                                                                                                                                                 
                                                                                                                                                                                                                                                                                                               
""")
f.close()
input()
