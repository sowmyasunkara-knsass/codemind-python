class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        ts = 0
        ds = 0
        for i in nums:
            ts = ts+i
            while(i!=0):
                r = i%10
                ds = ds+r
                i = i//10
        return ts-ds
