class Solution:
    def longestPalindrome(self, s):
        sub_s = s# holalola
        palindromos = []
        index = 0
        sub_s = s
        count = 0
        
        new_word = ""
        for letter in s:
            count += 1
            sub_s = s[count:]

            print("Word: {} to find: {}".format(sub_s,letter))
            n_count = sub_s.count(letter)
            if n_count < 1:
                
                continue
            
            for i in range(0, n_count - 1):
                index = sub_s[::].index(letter)#

                new_word = letter + sub_s[:index +1]

                ### NUEVO SUB_STRING
                sub_s = sub_s[index+1:]
                
                if new_word == new_word[::-1]:
                    #return new_word, sub_s, letter, sub_s[:index +1], index
                    print("FIND: {} - IN: {}".format(new_word, sub_s))
                    palindromos.append(new_word)
                #sub_s = sub_s[1:]
                
        return  palindromos

a = Solution()
s = "123498789555"
print(a.longestPalindrome(s))