class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if len(s2) < n:
            return False
        
        freq1 = [0] * 26
        freq2 = [0] * 26

        for ch in s1:
            freq1[ord(ch)-97] += 1
        
        l, r = 0, 0

        while r < n:
            freq2[ord(s2[r])-97] += 1
            if r == n-1:
                break
            r += 1
        
        if freq1 == freq2:
            return True

        while r < len(s2):
            i = l
            mismatch = False
            while i <= r:
                idx = ord(s2[i])-97
                if freq2[idx] != freq1[idx]:
                    l += 1
                    r += 1
                    mismatch = True
                    if r == len(s2):
                        break
                    freq2[ord(s2[l-1])-97] -= 1
                    freq2[ord(s2[r])-97] += 1
                     
                if mismatch:
                    break
                i += 1

            if not mismatch:
                return True
        
        return False