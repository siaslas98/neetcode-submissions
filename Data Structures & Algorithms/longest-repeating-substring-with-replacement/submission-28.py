class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        if k == n:
            return k
        
        l, r, max_count = 0, 1, 0
        res = 1
        freq = [0] * 26
        freq[ord(s[0]) - ord('A')] = 1
        max_count = 1

        while r < n:
            idx = ord(s[r]) - ord('A')
            freq[idx] += 1
            max_count = max(max_count, freq[idx])

            while (r-l+1) - max_count > k:
                freq[ord(s[l]) - ord('A')] -= 1
                l += 1
                continue

            res = max(res, r-l+1)
            r += 1

        return res
            


