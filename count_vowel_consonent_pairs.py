a=input()
v={'a','e','i','o','u','A','E','I','O','U'}
b=a[::-1]
c=0
for i in range(0,len(a)//2):
    if a[i].isalpha() and b[i].isalpha():
        if a[i] in v and b[i] not in v:
            c=c+1
        if b[i] in v and a[i] not in v:
            c=c+1
print(c)