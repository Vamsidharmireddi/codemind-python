a=input()
c=0
for i in a:
    if i.isalpha()==0 and i.isdigit()==0 and i!=" ":
        c=c+1
print(c)