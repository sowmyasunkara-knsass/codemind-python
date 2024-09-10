a,b = map(int,input().split())
list_of_primes = list(filter(lambda n: len([i for i in range(1,n+1) if n%i==0]) == 2,range(a,b+1)))
print(list_of_primes)
