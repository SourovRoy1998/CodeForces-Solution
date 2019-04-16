n=int(input())
L=[int(x) for x in input().strip().split(" ")]
x=len(set(L))
if x>3:
    print(-1)
elif x==1:
    print(0)
elif x==2:
    y=(max(L)-min(L))
    if(y/2==y//2):
        print(y//2)
    else:
        print(y)
else:
    L=list(set(L))
    L.sort()
    if(L[1]-L[0]==L[2]-L[1]):
        print(L[1]-L[0])
    else:
        print(-1)
