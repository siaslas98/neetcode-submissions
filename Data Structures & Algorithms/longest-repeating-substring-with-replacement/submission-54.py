import string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {char: 0 for char in string.ascii_uppercase}
        max_freq = 0
        res = 0

        l, r = 0, 0 

        while r < len(s):
            freq[s[r]] += 1
            max_freq = max(max_freq, freq[s[r]])

            windowSize = r-l+1
            replacements = windowSize - max_freq
            
            if replacements > k:
                # shrink the window
                freq[s[l]] -= 1
                l += 1
            else:
                res = max(res, windowSize)
            r += 1
    
        return res 

