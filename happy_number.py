def is_happy(n):
    s=0
    while n>0:
        d=n%10
        s=s+pow(d,2)
        n=n//10
    if s<=9:
        if s==1 or s==7:
            return 1
        else:
            return 0
    else:
        return is_happy(s)
n=int(input())
if is_happy(n):
    print('True')
else:
    print('False')