#This program sorts resistor readings into 1%, 5% or reject. Enter 0 to stop.

count_1 = 0
count_5 = 0
count_reject = 0

value = float(input("Enter measured resistance (0 to stop): "))

while value != 0:
    if value >= 99.0 and value <= 101.0:
        count_1 = count_1 + 1
    elif value >= 95.0 and value <= 105.0:
        count_5 = count_5 + 1
    else:
        count_reject = count_reject + 1
    value = float(input("Enter measured resistance (0 to stop): "))

print("1% tolerance:", count_1)
print("5% tolerance:", count_5)
print("Reject:", count_reject)
