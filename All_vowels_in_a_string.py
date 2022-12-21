n=input()
v={'a','e','i','o','u'}
c=[]
for i in v:
    if i not in n:
        print(False)
        break
else:
    print(True)