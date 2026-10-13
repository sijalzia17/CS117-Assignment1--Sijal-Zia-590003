#This program analyses a tuple of voltage readings for the following parameters
#a)count above 3.2 V
#b)highest
#c) lowest
#d) average

readings=(3.3, 3.1, 3.4, 2.9, 3.6, 3.0, 3.2)
count_above=0
highest=readings[0]
lowest = readings[0]
total = 0
for value in readings:
    if value > 3.2:  #analysing for count above 3.2 V
        count_above = count_above + 1
    if value > highest: #analysing for highest value
        highest = value 
    if value < lowest: #analysing for lowest value
        lowest = value
    total = total + value

average = total / len(readings) #analysing for average of all the values

print("Readings above 3.2 V:", count_above)
print("Highest reading:", highest, "V")
print("Lowest reading:", lowest, "V")
print("Average reading:",round(average,2), "V")
