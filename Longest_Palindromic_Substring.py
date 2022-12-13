a=input()
f=[]
for i in range(0,len(a)):
    s=""
    m=0
    for j in range(i,len(a)):
        s=s+a[j]
        if s==s[::-1]:
            c=s
            if len(c)>m:
                m=len(c)
    f.append(m)
z=max(f)
for i in range(0,len(a)):
    s=""
    m=0
    for j in range(i,len(a)):
        s=s+a[j]
        if s==s[::-1]:
            c=s
            if len(c)>m:
                m=len(c)
    if len(c)==z:
        print(c)
        break

        