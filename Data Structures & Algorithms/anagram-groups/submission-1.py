class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h_map = {}

        for s in strs:
            ch_list = [0] * 26
            for ch in s:
                idx = ord(ch) - ord('a')
                ch_list[idx] += 1
            iden = ""
            for i in range(26):
                iden += chr(i + ord('a')) * ch_list[i]
            
            if iden not in h_map:
                h_map[iden] = [s]
                continue
            
            h_map[iden].append(s)
        
        res = []

        for v in h_map.values():
            res.append(v)
        
        return res