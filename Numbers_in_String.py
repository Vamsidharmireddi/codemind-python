n=input()
m=0
for i in range(len(n)):
    if n[i].isdigit():
        m=m+int(n[i])
print(m)