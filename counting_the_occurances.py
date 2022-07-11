n=input()
k=input()
c=0
for i in range(len(n)):
    if k==n[i]:
        c=c+1
if c==0:
    print('-1')
else:
    print(c)