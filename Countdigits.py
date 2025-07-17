class Solution:
    def countDigits(self, num: int) -> int:
        c = 0
        t = num
        while(num!=0):
            r = num%10
            if t%r==0:
                c = c+1
            num = num//10
        return c
