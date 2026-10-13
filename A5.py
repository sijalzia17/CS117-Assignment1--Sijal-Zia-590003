# This program finds and prints the largest and smallest of three resistor values.


R1= int(input("Enter R1:"))
R2= int(input( "Enter R2:"))
R3= int(input( "Enter R3:"))
if R1>=R2 and R1>= R3:
    print( "largest=", R1,"ohm")
elif R2>= R1 and R2>=R3:
    print ( "largest=", R2, "ohm")
else:
    print ("largest=" ,R3, "ohm")

if R3<=R1 and R3<=R2:
    print( "smallest=",R3,"ohm")
elif R2<=R1 and R2<=R3:
        print ( "smallest=", R2, "ohm")
else:
    print ("smallest=",R1, "ohm")
        
        
    
