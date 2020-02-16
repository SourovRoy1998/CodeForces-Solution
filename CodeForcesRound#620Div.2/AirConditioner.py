for _ in range(int(input())):
    n,a=(int(x) for x in input().strip().split(" "))
    t,l,r=0,a,a
    L=[]
    for _z in range(n):
        L.append([int(x) for x in input().strip().split(" ")])

    ans=True
    for x in L:
        d=x[0]-t
        l1=l-d
        r1=r+d
        if x[2]<l1 or x[1]>r1:
            ans=False
            break
        l=max(x[1],l1)
        r=min(x[2],r1)
        t=x[0]
    if ans:
        print("YES")
    else:
        print("NO")
        
