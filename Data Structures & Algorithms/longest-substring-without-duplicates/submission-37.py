class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_set = set()
        max_len = 0

        l, r = 0, 0

        while r < len(s):
            if s[r] in char_set:
                while True:
                    if s[l] == s[r]:
                        if l == r-1:
                            l = r
                        else:
                            l += 1
                        break
                    else:
                        char_set.remove(s[l])
                    l += 1
            else:
                char_set.add(s[r])
                max_len = max(max_len, r-l+1)

            r += 1

        return max_len
        