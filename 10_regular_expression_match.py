class Solution:
    def isMatch(self, s, p):
        rules = []
        stack = ""
        output = True
        for letter in p:
            if letter == '*':
                stack = stack + letter
                rules.append(stack)
                stack = ""
            elif letter == '.':
                if stack != "":
                    rules.append(stack)
                    rules.append(letter)
                    stack = ""
                else:
                    rules.append(letter)
            
            else:
                stack = stack + letter

        if letter != '*' and letter != '.':
            rules.append(stack)
                
        
        count_rule = 0
        num_rules = len(rules)
        print('No. of rules: {}'.format(num_rules))
        print('Rules: {}'.format(rules))
        
        word = ''
        index = 0
        while count_rule < num_rules:
            print('---------------------------------------------------------- c:{}'.format(count_rule))
            rule_len = len(rules[count_rule])
            carry = 0
            if rules[count_rule][rule_len -1] == '*':
                carry = 1
            word = s[index: index + rule_len - carry]
            if rules[count_rule] == '.':
                word = s[index]
            
            print('Rule n: {} , is: {}, len: {}'.format(count_rule, rules[count_rule], rule_len))
            print('word::: {}  - from::: index: {} to index + len: {}'.format(word, index, index + rule_len - 1))

            if rules[count_rule][rule_len -1] == '*':
                print('Cerradura *   : {}   en: {}  ???'.format(rules[count_rule][0:rule_len -1], word))
                if rules[count_rule][0:rule_len -1] in word:
                    print('si hay un patron de *')
                    index += rule_len - 1
                    # No se incrementa el count_rule al poder encontrar otro patron.
                    continue
                else:
                    print('NO hay patron de *, Siguiente regla...')
                    count_rule += 1
                    continue

            if rules[count_rule][rule_len -1] in word:
                print('Estricto a: {}'.format(rules[count_rule]))
                index += rule_len - 1
                count_rule += 1
                continue

            if rules[count_rule][rule_len -1] == '.':
                print('Comodin')
                index += 1

                count_rule += 1
                continue

            if count_rule == num_rules:
                break
            else:
                return False#'x 1'


        if index < len(s) - 1:
            return False#'x 2'

        print("End class.")
        print("Rules: {}".format(rules))
        #if
        return output



s = "abcabcabcyesyeswab"
p = "abc*yes*.ab"
#s = "ap"
#p = "a."
zzz = Solution()
print('String::: {}    len::: {}'.format(s,len(s)))
print('Automata: {}'.format(p))
print('Output {}'.format(zzz.isMatch(s,p)))