from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        m1 = Counter(s1)
        window = {}

        for i in range(len(s1)):
            window[s2[i]] = window.get(s2[i], 0) + 1
        

        i, j = 0, len(s1)-1

        while j < len(s2):

            for k in range(i, j+1):
                if s2[k] in m1 and window[s2[k]] == m1[s2[k]]:
                    if k == j:
                        return True
                    continue
                else:
                    window[s2[i]] -= 1
                    i += 1
                    j += 1
                    if j < len(s2):
                        window[s2[j]] = window.get(s2[j], 0 ) + 1
                    break
        
        return False


        


