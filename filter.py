def is_odd(n):
    return n%2==1
n = [11,12,14,16,13]
f=filter(is_odd,n)
print(list(f))
