#This program converts the first resistor colour band into its digit (0-9)


colour=input("Enter the colour of first band of resistor:").strip().lower()

if colour == "black":
    print(0)
elif colour == "brown":
    print(1)
elif colour == "red":
    print(2)
elif colour == "orange":
    print(3)
elif colour == "yellow":
    print(4)
elif colour == "green":
    print(5)
elif colour == "blue":
    print(6)
elif colour == "violet":
    print(7)
elif colour == "grey":
    print(8)
elif colour == "white":
    print(9)
else:
    print("Invalid Colour")
