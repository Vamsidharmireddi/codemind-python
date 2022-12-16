n=input()
#print(n)
c=0
for i in n:
    if i==i.upper() and i!=' ':
        c+=1
print(c)