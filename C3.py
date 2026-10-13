# Function that converts a decimal number to a binary string.

def decimal_to_binary(n):
    Binary=""
    if n==0:
        return "0"
    for i in range(n):
        if n>0:
            Binary=str(n % 2) + Binary
            n = n // 2
    return Binary
n=int(input("Enter a number="))
print(decimal_to_binary(n))
