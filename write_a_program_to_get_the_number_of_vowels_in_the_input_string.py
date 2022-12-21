n=input()
v={'a','e','i','o','u','A','E','I','O','U'}
c=0
for i in n:
    if i in v:
        c=c+1
print(c)