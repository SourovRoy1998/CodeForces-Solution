t,m=(int(x) for x in input().strip().split(" "))
from collections import defaultdict
L=[]
for _ in range(t):
    L.append(input())
d=defaultdict(int)
left=""
right=""
mid=""


vis=set()
for x in L:
    d[x]+=1
for x,v in d.items():
    if x==x[::-1] and m*v>=len(mid):
        mid=x*v
    elif x not in vis and x[::-1] in d.keys():        
        e=min(d[x],d[x[::-1]])
        left=left+x*e
        right=e*x[::-1]+right
    vis.add(x[::-1])
ans=left+mid+right

print(len(ans))
if len(ans):print(ans)
        
        
    
