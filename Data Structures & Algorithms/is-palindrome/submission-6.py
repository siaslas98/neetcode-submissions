class Solution:
    def isPalindrome(self, s: str) -> bool:
        result = ''.join(c.lower() for c in s if c.isalnum())
        return result == result[::-1]

