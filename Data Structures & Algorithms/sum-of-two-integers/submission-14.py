class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a == 0: return b
        if b == 0 : return a

        bits = 32

        b_a = format(a & (2**bits - 1), 'b')
        b_b = format(b & (2**bits - 1), 'b')
        b_a = b_a.zfill(bits)
        b_b = b_b.zfill(bits)
        carry = 0

        for i in range(bits-1,-1,-1):
            s = int(b_a[i]) + int(b_b[i]) + carry

            if s == 0:
                carry = 0
            elif s == 1:
                b_a = b_a[:i] + '1' + b_a[i+1:]
                carry = 0
            elif s == 2:
                b_a = b_a[:i] + '0' + b_a[i+1:]
                carry = 1
            elif s == 3:
                carry = 1
                b_a = b_a[:i] + '1' + b_a[i+1:]

        if b_a[0] == '1':
            return int(b_a, 2) - 2**bits

        return int(b_a, 2)