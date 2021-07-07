class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        word = list()
        for letter in s:
            
            if letter not in word:
                word.append(letter)
                new_len = len(word)
                if new_len > output:
                    output = new_len
                
            else:
                word = word[word.index(letter) +1:]
                word.append(letter)
                new_len = len(word)
                if new_len > output:
                    output = new_len
                    if len(s) == 1:
            
        if len(s) == 1:
            return 1
        return output



"""
Success

Runtime: 72 ms, faster than 49.20% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.5 MB, less than 6.64% of Python3 online submissions for Longest Substring Without Repeating Characters.

"""

"""
whitout the if of line 21-22 :

Runtime: 60 ms, faster than 75.77% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.4 MB, less than 24.00% of Python3 online submissions for Longest Substring Without Repeating Characters.

"""


###  2ND VERSION ::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        word = list()
        for letter in s:
            
            if letter not in word:
                word.append(letter)
                
            else:
                word = word[word.index(letter) +1:]
                word.append(letter)
                
            new_len = len(word)
            output = new_len if new_len > output else output
            if new_len > output:
                output = new_len

        return output

"""
Success
Runtime: 64 ms, faster than 66.40% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.3 MB, less than 78.54% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""


####  3rd VERSION f in one line::::::::::::::::::::::::::::::::::::::::
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        output = 0
        word = list()
        for letter in s:
            
            if letter not in word:
                word.append(letter)
                
            else:
                word = word[word.index(letter) +1:]
                word.append(letter)
                
            new_len = len(word)
            output = new_len if new_len > output else output
        return output

"""
Runtime: 68 ms, faster than 56.71% of Python3 online submissions for Longest Substring Without Repeating Characters.
Memory Usage: 14.3 MB, less than 53.12% of Python3 online submissions for Longest Substring Without Repeating Characters.
"""