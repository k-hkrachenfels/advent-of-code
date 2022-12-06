
count=0
count_intersect=0
for line in open("i.txt"):
    line = line.strip()
    line = line.split(",")
    ranges = [list(rng.split("-")) for rng in line]
    a,b = [set(range(int(a),int(b)+1)) for a,b in ranges]
    print(a,b)
    if a.issubset(b) or b.issubset(a):
        count+=1
    if len(a.intersection(b))>0:
        count_intersect+=1
print(count, count_intersect)