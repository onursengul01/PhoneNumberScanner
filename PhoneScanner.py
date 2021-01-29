# This program is an automation(I made it simpler to use for users) of a program called PhoneInfoga and it is used to scan phone 
# numbers such and find  their country, area, carrier and line type. I made it simpler to use it hope you find my automation usefull.
# This program works on linux and in the future i will make it compatible for windows. 
 

import os
import os.path
import sys

if os.getuid() != 0:
	print("Sorry. This script requires sudo privledges")
	sys.exit()

class PhoneTracker:
    def PhoneInfogaCheker(self):
        global path
        path = '/usr/bin/Phoneinfoga'
        gitRepo = 'https://github.com/la-deep-web/Phoneinfoga'
        if os.path.exists(path):
            return s.UserInput()
        else:
            os.system("clear")
            os.system(f"git clone {gitRepo} {path}")
            os.system("clear")
            os.system(f"pip3 install -r {path}/requirements.txt")
            return s.UserInput()
    def UserInput(self):
        os.system("clear")
        phoneNumber = input("Enter a phone number to track (if its an international phone number ex: 1+006589876): ")
        os.system("clear")
        os.system(f"python3 {path}/phoneinfoga.py -n {phoneNumber}")
        return s.PressEnter()

    def PressEnter(self):
        enter = input("press enter to scan more phone numbers\n")
        if enter == "":
            return s.UserInput()

        else:
            s.PressEnter()



s = PhoneTracker()


if __name__ == "__main__":
    try:
        s.PhoneInfogaCheker()

    except KeyboardInterrupt:
        print("\n")
        sys.exit()
