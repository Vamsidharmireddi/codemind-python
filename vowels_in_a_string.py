n=input()
a=input()
for i in range(0,len(n)):
    if n[i]==a:
        print(True)
        print(i)
        break
else:
    print(False)