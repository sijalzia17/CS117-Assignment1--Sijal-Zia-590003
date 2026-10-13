# This program has a function that returns the total resistance of resistors connected in parallel.

def parallel_resistance(resistors):
    total = 0
    for r in resistors:
        total = total + 1/ r
    return round(1 / total, 2)

print(parallel_resistance([10,10]))
print(parallel_resistance([100,200,300]))
