n,x,y=map(int,input().strip().split(" "))
L=list(map(int,input().strip().split(" ")))


for i in range(len(L)):
    x_min=10000000000
    y_min=10000000000

    for j in range(i-1,max(-1,i-x-1),-1):
        x_min=min(x_min,L[j])
    for j in range(i+1,min(n,i+1+y)):
        y_min=min(y_min,L[j])
    if(x_min>L[i] and y_min>L[i]):
        print(i+1)
        break
