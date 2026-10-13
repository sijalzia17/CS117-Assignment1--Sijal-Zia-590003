#This program calculates current from voltage and resistance and warns if the fuse will blow at currents greater than 2A.

voltage=float(input("Enter Voltage (V):")) #
resistance=float(input("Enter Resistance (ohm):"))
if resistance<=0:
    print('Invalid Resistance')
else:
     current= voltage / resistance
     print("current=",current,"A")
     if current > 2:
        print("Fuse will blow")
     else:
        print("Circuit is safe")
