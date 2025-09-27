import math
class Solution:
    def reverseexponentiation(self, n):
        a = str(n)[::-1]
        b = int(a)
        return int(math.pow(n,b))
