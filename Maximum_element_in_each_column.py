R,C=map(int,input().split())
l=[]
for i in range(R):
    k=list(map(int,input().split()))
    l.append(k)
for i in range(C):
    s=0
    for j in range(R):
        if l[j][i]>s:
            s=l[j][i]
    print(s)