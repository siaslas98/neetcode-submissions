class Solution:
    def hammingWeight(self, n: int) -> int:
        b_string = format(n, 'b')
        res = 0
        for num_ch in b_string:
            if num_ch == '1':
                res += 1
        return res