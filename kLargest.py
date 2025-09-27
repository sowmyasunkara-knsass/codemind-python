class Solution:
	def kLargest(self, arr, k):
	    a = sorted(arr,reverse = True)
	    return a[:k]
