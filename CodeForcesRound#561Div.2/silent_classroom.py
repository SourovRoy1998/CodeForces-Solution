##https://codeforces.com/contest/1166/problem/A
from collections import defaultdict
d=dict()
for _ in range(int(input())):
    x=input()[0]
    d[x]=d.get(x,0)+1

ans=0    
for value in d.values():
    x=value//2
    y=value-x
    ans=ans+x*(x-1)//2+y*(y-1)//2
print(ans)
