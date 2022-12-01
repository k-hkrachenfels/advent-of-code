import numpy as np

elves = []
acc_cal=0
for line in open("input_calories.txt"):
    t = line.split()
    if len(t)==0: 
        if acc_cal!=0:
            elves.append(acc_cal)
            acc_cal=0
        continue    
    acc_cal += int(t[0]) 
    
elves.sort()
top_three = elves[-3:]
top_three = np.array(top_three)
print(top_three)
print(np.sum(top_three))

    
    
