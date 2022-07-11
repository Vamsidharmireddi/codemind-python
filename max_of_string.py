n=input()
ma='A'
for i in range(len(n)):
    z=ord(n[i])
    if z>ord(ma):
        ma=n[i]
print(ma)
