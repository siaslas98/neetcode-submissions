class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        res = 1

        l, r = 0, 1
        h_map = {
            s[l] : 0
        }

        while r < len(s):
            if s[r] in h_map and h_map[s[r]] >= l:
                index = h_map[s[r]]
                l = index + 1
            else:
                res = max(res, r-l+1)
                print(r-l+1)

            h_map[s[r]] = r
            r += 1
        
        return res



