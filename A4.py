# This program takes two bits (0 or 1) and prints the results of logic gates AND, OR and XOR .

A=int(input("Enter A:"))
B=int(input("Enter B:"))
if (A !=1 and A!=0)or (B !=0 and B!=1):
    print("Bits must be 0 or 1")
else:
    if A==1 and B==1:
        print ( "AND=1")
        print ( "OR=1")
        print ( "XOR=0")
    elif A==1 and B==0:
        print ( "AND=0")
        print ( "OR=1")
        print ( "XOR=1")
    elif A==0 and B==1:
        print ( "AND=0")
        print ( "OR=1")
        print ( "XOR=1")
    else:
        print ( "AND=0")
        print ( "OR=0")
        print ( "XOR=0")
     
