class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        res = []

        for s in strs:
            anagram = tuple(sorted(s))
            if anagram in mp:
                mp[anagram].append(s)
            else:
                mp[anagram] = [s]
        
        for anagram, sublist in mp.items():
            res.append(sublist)
        
        return res

                