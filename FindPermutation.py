from itertools import permutations
class Solution:
    def findPermutation(self, s):
        c = permutations(s)
        d = set([''.join(i) for i in c])
        return sorted(d)
