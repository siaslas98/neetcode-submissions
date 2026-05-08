class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        mp = Counter(s)

        for ch in t:
            if ch not in mp:
                return False
            mp[ch] -= 1
        
        for ch, count in mp.items():
            if count != 0:
                return False
        
        return True
