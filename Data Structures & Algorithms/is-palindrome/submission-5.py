class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c.lower() for c in s if c.isalnum())
        result_cpy = result[::-1]

        print([result, result_cpy])
        return result == result_cpy

