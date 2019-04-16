//https://codeforces.com/contest/1154/problem/C

a,b,c=(int(x) for x in input().strip().split(" "))
n=min(a//3,b//2,c//2)
ans=n*7

a=a-n*3
b=b-n*2
c=c-n*2

#print(a,b,c)
L=['r','f','f','r','c','f','c','r','f','f','r','c','f','c']

i=0
max_count=0
while(i<7):
    x=a
    y=b
    z=c
    j=i
    i+=1
    count=0
    while(j<14):
        if(x>0 and L[j]=='f'):
            x-=1
            count+=1
        elif(y>0 and L[j]=='r'):
            y-=1
            count+=1
        elif(z>0 and L[j]=='c'):
            z-=1
            count+=1
        else:
            break
        max_count=max(count,max_count)
        j+=1
ans+=max_count
print(ans)
