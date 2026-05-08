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
            r += 1
        
        if freq1 == freq2:
            return True
        
        while r < len(s2):
            # Remove the leftmost character from the window
            freq2[ord(s2[l])-97] -= 1
            l += 1
            
            # Add the new character to the window
            freq2[ord(s2[r])-97] += 1
            r += 1
            
            if freq1 == freq2:
                return True
        
        return False