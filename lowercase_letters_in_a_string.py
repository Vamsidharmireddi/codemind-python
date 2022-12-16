n=input()
#print(n)
c=0
for i in n:
    if i==i.lower() and i!=' ':
        c+=1
print(c)