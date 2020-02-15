for _ in range(int(input())):
    s=input()
    if len(set(s))==1:
        print(0)
    else:
        flag=False
        for i in range(len(s)):
            if s[i]=='1':
                if not flag:
                    x=i
                    flag=True
                y=i
        print((y-x+1)-s.count("1"))
        
