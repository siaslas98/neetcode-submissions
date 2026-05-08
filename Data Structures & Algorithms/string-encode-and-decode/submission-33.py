class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_s = ""

        for s in strs:
            encoded_s += str(len(s)) + "_" + s
        
        return encoded_s


    def decode(self, s: str) -> List[str]:

        strs = []
        length_str = ""
        i = 0

        while i < len(s):
            if s[i].isdigit():
                length_str += s[i]
            elif s[i] == "_":
                length = int(length_str)
                strs.append(s[i+1:i+1+length])
                i += (1 + length)
                length_str = ""
                continue
            i += 1

        return strs





