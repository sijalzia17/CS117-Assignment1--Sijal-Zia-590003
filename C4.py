# Function that calculates a voltage divider's output with and without a load resistor.

def loaded_divider(vs,r1,r2,rl):
    v_unloaded= vs* r2 / (r1+r2)
    r_parallel= (r2 *rl ) / (r2 +rl)
    v_loaded = vs * r_parallel / (r1 + r_parallel)
    return v_unloaded, v_loaded

v_ideal, v_actual = loaded_divider(12, 1000, 1000, 500)
print("Unloaded voltage =", round(v_ideal, 2), "V")
print("Loaded voltage =", round(v_actual, 2), "V")
