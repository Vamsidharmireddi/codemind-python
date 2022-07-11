n=input()
c=0
for i in range(len(n)):
    if n[i].isdigit():
        c=c+1
if c==0:
    print("Doesn't contain digit")
else:
    print('Contains',c,'digit',end='')