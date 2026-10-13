#This program prints a table of current for voltages 1-10 V across a 10 ohm resistor (Ohm's law).

r= 10
print (r)
for v in range(1,11):
    I = v / r
    print("V=", v , "V","I=",I,"A")
    
