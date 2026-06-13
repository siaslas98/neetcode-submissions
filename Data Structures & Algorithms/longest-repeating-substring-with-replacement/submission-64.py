class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == k:
            return k
        
        maxLength, maxCount = k, 1
        h_map = {}
        i, j = 0, k

        for x in range(k):
            h_map[s[x]] = h_map.get(s[x], 0) + 1
            maxCount = max(maxCount, h_map[s[x]])
        
        while j < len(s):
            h_map[s[j]] = h_map.get(s[j], 0) + 1
            maxCount = max(maxCount, h_map[s[j]])
            length = j - i + 1
            replacements = length - maxCount

            while replacements > k and i < j:
                h_map[s[i]] -= 1
                i += 1
                length -= 1
                replacements = length - maxCount

            
            maxLength = max(maxLength, length)

            j += 1
        
        return maxLength




                







