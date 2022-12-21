s1=input()
s2=input()
a=set(s1.lower())
b=set(s2.lower())
for i in a:
    if i not in b:
        print(False)
        break
else:
    print(True)