for _ in range(int(input())):
    x,y,a,b=(int(x) for x in input().strip().split(" "))
    if (y-x)%(a+b)==0:
        print((y-x)//(a+b))
    else:
        print(-1)
