n=int(input())
add=0
p=1
while n>0:
    d=n%10
    add=add+d
    p=p*d
    n=n//10
print(abs(add-p))