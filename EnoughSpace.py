x = int(input())
for i in range(1,x+1):
    a,b,c  = map(int,input().split())
    if (b+(2*c))<=a:
        print("YES")
    else:
        print("NO")
