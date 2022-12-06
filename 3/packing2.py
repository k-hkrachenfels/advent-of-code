
val=0
with open("ii.txt") as f:
    while True:
        l1 = f.readline().strip()
        if len(l1)==0:
            break
        l2 = f.readline().strip()
        l3 = f.readline().strip()
        print(l1)
        print(l2)
        print(l3)
        s1={s for  s in l1}
        s2={s for  s in l2}
        s3={s for  s in l3}
        its = s1.intersection(s2).intersection(s3)
        if len(its)!=1:
            raise Exception("unexpected  intersection")
        it = its.pop()
        print(it)
        if it>="a" and it<="z":
            itval=1+ord(it)-ord("a")
        else:
            itval=27+ord(it)-ord("A")
        print(itval)
        val+=itval
print(val)