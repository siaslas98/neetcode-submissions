class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        i = 0

        while i < len(strs):
            count = 1
            while i + 1 < len(strs) and strs[i+1] == strs[i]:
                count += 1
                i += 1
            encoded_str += str(count) + "__" + strs[i] + "__"
            i += 1

        return encoded_str[:-2]

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded_s_list = s.split('__')
        final_list = []

        for i in range(0, len(decoded_s_list), 2):
            for j in range(int(decoded_s_list[i])):
                final_list.append(decoded_s_list[i+1])
        
        return final_list

