n=int(input())
a=[]
while n>0:
    d=n%10
    a.append(d)
    n=n//10
if len(set(a))==len(a):
    print('Unique Number')
else:
    print('Not Unique Number')