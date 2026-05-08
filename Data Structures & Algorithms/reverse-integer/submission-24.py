class Solution:
    def reverse(self, x: int) -> int:
        # Determine the sign and work with the absolute value
        sign = -1 if x < 0 else 1
        x_abs = abs(x)
        
        # Reverse using string slicing
        reversed_str = str(x_abs)[::-1]
        
        # Convert back to integer and reapply the sign
        reversed_int = sign * int(reversed_str)
        
        # Check the 32-bit signed integer range
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
        return reversed_int


        


