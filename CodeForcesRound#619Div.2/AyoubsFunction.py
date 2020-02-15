import sys
input = lambda: sys.stdin.readline().rstrip()
for _ in range(int(input())):
    (n,m)=(int(x) for x in input().strip().split(" "))
    g=m+1
    z=n-m
    k=z//g
    print(n*(n+1)//2-g*k*(k+1)//2-(k+1)*(z%g))
