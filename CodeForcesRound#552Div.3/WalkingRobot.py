//https://codeforces.com/contest/1154/problem/D

n,b,a=(int(x) for x in input().strip().split(" "))
L=[int(x) for x in input().strip().split(" ")]
ans=0

battery=b
acc=a
for x in L:
    if(x==1 and acc<a and battery>0):
        if(battery==0):
            break
        battery-=1
        acc+=1
        ans+=1
    elif(x==1 and acc==a):
        acc-=1
        ans+=1
    else:
        if(acc>0):
            acc-=1
            ans+=1
        elif(battery>0):
            battery-=1
            ans+=1
        else:
            break
print(ans)
        
