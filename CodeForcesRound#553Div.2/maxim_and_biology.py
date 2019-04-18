def distance(A,B):
    return min(abs(ord(A)-ord(B)),26-abs(ord(A)-ord(B)))

input()
string=input()

ans=200

for i in range(len(string)-3):
    ans=min(ans,distance('A',string[i])+distance('C',string[i+1])+distance('T',string[i+2])+distance('G',string[i+3]))
print(ans)
