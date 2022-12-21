a=input()
k=set(a)
for i in k:
    if a.count(i)!=1:
        print(False)
        break
else:
    print(True)