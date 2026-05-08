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
        window = {}
        
        l, r = 0, 0 

        while r < n1:
            window[s[r]] = window.get(s[r], 0) + 1

            if contains(window, freq1):
                if min_length == None:
                    min_length = r-l+1
                    res = s[l:r+1]
                elif r-l+1 < min_length:
                    min_length = r-l+1
                    res = s[l:r+1]
                
                while l <= r and contains(window, freq1):
                    if r-l+1 < min_length:
                        min_length = r-l+1
                        res = s[l:r+1]
                    window[s[l]] -= 1
                    l += 1
            r+=1
        
        return res



