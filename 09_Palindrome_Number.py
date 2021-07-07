"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        palindrome = str(x)
        if str(x) == palindrome[::-1]:
            return True
        else:
            return False

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return False if x < 0 else x == int(str(x)[::-1])

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]


"""
Runtime: 52 ms, faster than 89.16% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.3 MB, less than 47.40% of Python3 online submissions for Palindrome Number.
------
Agregando el if en la linea 9 para saltar los valores negativos:
Runtime: 48 ms, faster than 95.11% of Python3 online submissions for Palindrome Number.
Memory Usage: 14.2 MB, less than 75.71% of Python3 online submissions for Palindrome Number.
"""

