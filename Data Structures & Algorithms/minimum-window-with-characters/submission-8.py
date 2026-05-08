class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def contains(freq2, freq1):
            return all(freq2.get(c, 0) >= freq1[c] for c in freq1) 

        n1 = len(s)
        n2 = len(t)
        min_length = None
        res = ""

        if n1 < n2:
            return ""

        freq1 = Counter(t)
        freq2 = {}
        l, r = 0, 0 

        # Grow window to n2 characters long, counting frequency of each unique char in s
        while r < n2:
            freq2[s[r]] = freq2.get(s[r], 0) + 1
            r += 1
        
        # SPECIAL CASE: FIRST PART OF STRING MATCHES PERFECTLY
        if contains(freq2, freq1):
            return s[0:r]

        while r < n1:
            freq2[s[r]] = freq2.get(s[r], 0) + 1

            if contains(freq2, freq1):
                if min_length == None:
                    min_length = r-l+1
                    res = s[l:r+1]
                elif r-l+1 < min_length:
                    min_length = r-l+1
                    res = s[l:r+1]
                
                while l <= r and contains(freq2, freq1):
                    min_length = r-l+1
                    res = s[l:r+1]
                    freq2[s[l]] -= 1
                    l += 1
            r+=1
        
        return res



