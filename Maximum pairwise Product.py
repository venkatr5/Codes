#Python3
a=input()
b=list(map(int,input().split()))
c=0
d=0
for i in range(len(b)):
    if (b[i]>c):
        c=b[i]
for j in range(len(b)):
    if (b[j]>d and b[j]!=c):
        d=b[j]
print(c*d)