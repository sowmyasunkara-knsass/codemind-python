class Solution:
    def replaceDigits(self, s: str) -> str:
        s = list(s)
        for i in range(1,len(s),2):
            if s[i].isdigit():
                a = int(s[i])
                s[i]= chr(ord(s[i-1])+a)
        res = "".join(s)
        return res
