a=input()
k=a.upper()
c=0
for i in range(0,len(a)):
    if a[i]==k[i] and a[i]!=" ":
        c=c+1
print(c)