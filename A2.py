#This program shows the direction of current flow based on whether the current is positive, zero or negative.

current=int(input("Enter Current(A):"))
if current>0:
    print("Current flows from A to B")
elif current==0:
    print("No current flows")
else:
    print("Current flows from B to A")
            
