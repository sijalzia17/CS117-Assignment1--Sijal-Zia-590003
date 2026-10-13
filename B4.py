#This programs finds the longest continuous drop in a list of battery voltages and where it starts and ends


voltages = [12.6, 12.5, 12.5, 12.3, 12.1, 11.9, 12.0, 11.8, 11.6, 11.5, 11.5, 11.2]
streak = 1
best = 1
best_end = 0

for i in range(1, len(voltages)):
    if voltages[i] < voltages[i - 1]:
        streak = streak + 1
    else:
        streak = 1

    if streak > best:
        best = streak
        best_end = i

best_start = best_end - best + 1

print("Longest continuous drop:", best, "voltages")
print("Started at:", voltages[best_start], "V")
print("Ended at:", voltages[best_end], "V")
