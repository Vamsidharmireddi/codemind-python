n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in s:
        if i.isdigit():
            print('Yes')
            break
    else:
        print('No')