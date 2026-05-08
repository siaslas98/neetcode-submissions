class Solution:
    def reverseBits(self, n: int) -> int:
        bit_string = format(n, 'b')
        bit_string = bit_string.zfill(32)
        return int(bit_string[::-1], 2)