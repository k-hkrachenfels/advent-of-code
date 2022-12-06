from collections import deque, defaultdict

dqs = defaultdict(deque)
for line in open("ii0.txt"):
    line.strip()
    #print(line)
    #print(len(line))
    for i,cidx in enumerate(range(0,len(line),4)):
        character = line[cidx+1]
        if character== " ":
            continue
        else:
            dqs[i].appendleft(character)

#for i in range(len(dqs)):
#    print(dqs[i])

for line in open("ii1.txt"):
    line.strip()
    _, numc,_,sourceloc,_,targetloc = line.split()
    sourceloc = int(sourceloc) - 1
    targetloc = int(targetloc) - 1
    print(numc,sourceloc,targetloc)
    tmp = deque()
    for _ in range(int(numc)):
        item = dqs[sourceloc].pop()
        tmp.append(item)

    for _ in range(len(tmp)):    
        item = tmp.pop()
        dqs[targetloc].append(item)

for i in range(len(dqs)):
    item = dqs[i].pop()
    print(item,end="")
print()
    