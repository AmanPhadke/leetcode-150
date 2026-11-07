class Solution(object):
    def reverseWords(self, s):
        l = 0
        sentence = ''

        s = s[::-1]

        while l < len(s):
            word = ''
            while (l < len(s)) and (s[l] != ' '):
                word += s[l]
                l += 1
            
            if len(word) > 0:
                word = word[::-1]
                sentence += ' ' + word
            

            
            l += 1

        return sentence[1:]
