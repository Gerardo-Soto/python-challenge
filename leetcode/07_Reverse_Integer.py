"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:
        
        if abs(x) > (2 ** 31) -1:
            return 0
        
        if x >= 0:
            output = str(x)
            output = output[::-1]
            return int(output)
            
        else:
            output = str(x)
            output = output[1::]
            output = output[::-1]
            output = "-" + output
            return int(output)
            

"""
Runtime: 36 ms, faster than 42.25% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.4 MB, less than 10.59% of Python3 online submissions for Reverse Integer.

--- 2 comentarios menos:
Memory Usage: 14.2 MB, less than 42.92% of Python3 online submissions for Reverse Integer.

--- quitando el return al final y agregarcelo a cada caso:
Runtime: 28 ms, faster than 89.26% of Python3 online submissions for Reverse Integer.
Memory Usage: 14.2 MB, less than 72.17% of Python3 online submissions for Reverse Integer.
"""
