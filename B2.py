# This program adds up the resistor values entered by the user to get the total series resistance.

count=int(input("How many resistors in series?"))
total=0
for i in range (count):
    value =float(input("Enter resistor value in ohms: "))
    total = total + value

print("Total resistance:", total, "ohms") 
    
    
    
