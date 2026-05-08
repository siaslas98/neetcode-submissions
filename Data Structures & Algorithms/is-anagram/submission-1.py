class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        r1 = [0] * 26
        r2 = [0] * 26

        for ch in s:
            r1[ord(ch) - ord('a')] += 1
        for ch in t:
            r2[ord(ch) - ord('a')] += 1
        
        for i in range(len(r1)):
            if r1[i] != r2[i]:
                return False
        return True


       
    


