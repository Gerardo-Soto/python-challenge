class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text
        
        index_text = 0
        pattern = pattern[::-1]
        text = text[::-1]
        print(pattern,text)

        for letter in range(len(pattern)):
            if pattern[letter] == '.':
                index_text += 1

            elif pattern[letter] == '*':
                ########try
                if pattern[letter + 1] = '.':

                else:
                    search = True
                    while search:
                        if text[index_text] == pattern[letter + 1]


            else:
                if text[index_text] == pattern[letter]:
                    index_text += 1
                else:
                    return "False -- 1"


#s = "abcccccyosssssssswab"
#p = "abc*yes*.ab"
s = "bbc"
p = "a*b*c"
zzz = Solution()
print('String::: {}    len::: {}'.format(s,len(s)))
print('Automata: {}'.format(p))
print('Output {}'.format(zzz.isMatch(s,p)))