class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return f"1#{len(strs[0])}:{strs[0]}"

        count = 1
        res = ""

        for i in range(1, len(strs)):
            if strs[i] == strs[i-1]:
                count += 1
            else:
                res += f"{count}#{len(strs[i-1])}:{strs[i-1]}"
                count = 1

        res += f"{count}#{len(strs[-1])}:{strs[-1]}"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            digits = ""
            while i < len(s) and s[i].isdigit():
                digits += s[i]
                i+=1
            count = int(digits)

            i+=1 

            digits = ""
            while i < len(s) and s[i].isdigit():
                digits += s[i]
                i+=1
            length = int(digits)

            i+=1

            cur_str = s[i:i+length]
            i += length
            
            res.extend([cur_str] * count)
        
        return res

            
