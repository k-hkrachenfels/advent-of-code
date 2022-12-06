from collections import deque

def first_index(line):
    d = deque(maxlen=14)
    for i,character in enumerate(line):
        d.append(character)
        s=set(d)
        if len(s)==14:
            return i+1
    return -1


for line in open("i.txt"):
    print(first_index(line))
