class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if not n:
            return 0
        l, r = 0, 1
        res = 1
        b = {s[0]:0}

        while r < n:
            if s[r] in b and b[s[r]] >= l:
                res = max(res, r-l)
                l = b[s[r]] + 1
                b[s[l]] = l   
            b[s[r]] = r
            r += 1
                
        res = max(res, r-l)
        return res