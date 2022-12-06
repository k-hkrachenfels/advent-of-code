
val=0
for line in open("ii.txt"):
    s = line.strip()
    print(s)
    l = len(s)
    if l==0:
        continue
    c1=s[:l//2]
    c2=s[l//2:]
    s1={s for  s in c1}
    s2={s for  s in c2}
    print(c1)
    print(c2)
    print(f"{s1},{s2}")
    its = s1.intersection(s2)
    if len(its)==0:
        exit()
    it = its.pop()
    print(it)
    if it>="a" and it<="z":
        itval=1+ord(it)-ord("a")
    else:
        itval=27+ord(it)-ord("A")
    print(itval)
    val+=itval
print(val)