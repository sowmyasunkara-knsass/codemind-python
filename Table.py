def table(n,r):
    for i in range(1,r+1):
        print(n,"*",i,"=",(n*i))
n=int(input())
r=int(input())
table(n,r)
