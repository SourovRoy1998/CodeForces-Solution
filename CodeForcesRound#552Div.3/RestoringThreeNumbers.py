##https://codeforces.com/contest/1154/problem/A

p,q,r,s = (int(x) for x in input().strip().split(" "))
temp=(p+q+r+s)//3

if(p!=temp):
    print(temp-p,end=" ")
if(q!=temp):
    print(temp-q,end=" ")
if(r!=temp):
    print(temp-r,end=" ")
if(s!=temp):
    print(temp-s,end=" ")
