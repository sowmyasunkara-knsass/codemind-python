from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = Counter(s)
        for i in s:
            if a[i]==1:
                return s.index(i)
        return -1
