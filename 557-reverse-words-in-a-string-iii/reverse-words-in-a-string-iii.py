class Solution(object):
    def reverseWords(self, s):
        l = 0
        sentence = ''

        while l < len(s):
            word = ''
            while (l < len(s) and s[l] != ' '):
                word += s[l]
                l += 1

            
            if len(word) > 0:
                sentence += ' ' + word[::-1]

            l += 1
            

        return sentence[1:]


        