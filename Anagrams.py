a=input()
b=input()
x=a.lower()
y=b.lower()
p=set(x)
q=set(y)
if p==q:
    print('True')
else:
    print('False')