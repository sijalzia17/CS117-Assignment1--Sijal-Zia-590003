#Function that converts a Star (Y) resistor network into its equivalent Delta network.

def star_to_delta(ra, rb, rc):
    n = ra * rb + rb * rc + rc * ra

    rab = n / rc
    rbc = n / ra
    rca = n / rb

    return round(rab, 2), round(rbc, 2), round(rca, 2)


print(star_to_delta(10, 20, 30))
