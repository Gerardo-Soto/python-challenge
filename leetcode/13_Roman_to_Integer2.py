'''
Author: Soto Alvarez del Castillo Gerardo Alberto.
e-mail: gerardo.8.soto@gmail.com
Source: LeetCode
Program: 13 Roman to Integer
Data:
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two one's added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Version: 1.0
Date: 7-Jul-21
Comments:
'''

class Solution:
    def romanToInt(self, s):
        symbols = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        output = 0
        for letter in range(len(s) - 1):
            if symbols[s[letter]] >= symbols[s[letter + 1]]:
                output += symbols[s[letter]]
            else:
                output -= symbols[s[letter]]
                
            
        output += symbols[s[len(s) - 1]]
        return output

if __name__ == '__main__':
    testCase = ["XIV","CXLIX","IV","LVIII","MCMXCIV"]
    problem = Solution()
    for test in testCase:
        print("Sol: {}".format(problem.romanToInt(test)))


"""
Success
Runtime: 40 ms, faster than 92.80% of Python3 online submissions for Roman to Integer.
Memory Usage: 14.4 MB, less than 25.07% of Python3 online submissions for Roman to Integer.
"""
