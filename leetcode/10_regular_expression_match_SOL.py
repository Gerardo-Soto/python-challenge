class Solution(object):
    def isMatch(self, text, pattern):
        if not pattern:
            return not text

        first_match = bool(text) and pattern[0] in {text[0], '.'}

        if len(pattern) >= 2 and pattern[1] == '*':
            return (self.isMatch(text, pattern[2:]) or
                    first_match and self.isMatch(text[1:], pattern))
        else:
            return first_match and self.isMatch(text[1:], pattern[1:])



s = "abcccccyosssssssswab"
p = "abc*yes*.ab"
#s = "qwertgy"
#p = ".*"
zzz = Solution()
print('String::: {}    len::: {}'.format(s,len(s)))
print('Automata: {}'.format(p))
print('Output {}'.format(zzz.isMatch(s,p)))