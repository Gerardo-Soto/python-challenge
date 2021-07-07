class Solution:
    def longestPalindrome(self, s):
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s == s[::-1]:
                return s
            else:
                return s[0]

        len_pal = 0
        output = s[0]
        operaciones = 0

        for i in range(0,len(s) - 1):
            print("letter {} = {}".format(i,s[i]))
            # If the letter is unique: continue
            letters = s[i + 1:].count(s[i])
            if letters < 1:
                continue
            
            for j in range(i+1, len(s) - 0):
#            j = i+1
#            print("letters::: {}".format(letters))
#            while letters != 0:
                operaciones += 1 
                if s[i] == s[j]:
                    letters -= 1
                    is_pal = s[i:j+1]
                    print("Is Pal?: {}".format(is_pal))
                    if is_pal == is_pal[::-1]:
                        if len(is_pal) > len_pal:
                            len_pal = len(is_pal)
                            output = is_pal

 #               j += 1
        
        print(operaciones)                    
        return output

a = Solution()
s = ["abcda",
"abcdedcbf",
"abababeiouuoieq",
"sldfghjhgfdws"]
print(s[1])
print("Sol: {}".format(a.longestPalindrome(s[1])))

"""
Runtime: 5484 ms, faster than 25.22% of Python3 online submissions for Longest Palindromic Substring.
Memory Usage: 14.2 MB, less than 81.35% of Python3 online submissions for Longest Palindromic Substring.
"""