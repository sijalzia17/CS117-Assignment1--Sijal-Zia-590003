#This program uses functions to calculate current (I = V/R) and power (P = I^2 * R).

def ohms_current(v,r):
    "Return current in amps using ohm's law I= V / R "
    return v / r


def power_dissipated(i,r):
    "Return power in watts using P=I^2 * R"
    return i** 2 *r

V= 12 
R= 6 

current= ohms_current(V,R)
Power= power_dissipated(current,R)

print("Current=", current,"A")
print("Power=" , Power , "W")
