for _ in range(int(input())):
    a,b,c=input(),input(),input()
    ans=True
    for i in range(len(a)):
        if not(c[i]==b[i] or c[i]==a[i]):
            ans=False
    if ans:
        print("YES")
    else:
        print("NO")
