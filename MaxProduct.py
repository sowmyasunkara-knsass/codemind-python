class Solution:
    def maxProduct(self, arr):
        arr.sort()
        return max(arr[-1]*arr[-2]*arr[-3],arr[0]*arr[1]*arr[-1])
