import RPi.GPIO as GPIO
import time
import sys


# A line that starts with '#' will be ignored by the computer.
# These lines are called comments.
# They are for humans reading the code.

# The print function displays the characters in quotations.
print("Hello World")

# Wait 1 second before continuing
time.sleep(1)
# Enter your name
name = "ivan"

print("name: "+name)

crowpi_version = 2

crowpi_version = 2.0

had_breakfast = True
had_dinner = False

if(had_breakfast == True):
    hungry = False
else:
    hungry = True

print("Is "+name+" hungry: "+str(hungry))

if(crowpi_version == 2):
    new_crowpi = True
else:
    new_crowpi = False
print("Is this a new CrowPi?: "+str(new_crowpi))

number = 0 
while True:
    number = number + 1
    print(number)
    time.sleep(1)

sys.exit()