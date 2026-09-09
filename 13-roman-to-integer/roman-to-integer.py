class Solution(object):
    def romanToInt(self, s):
        roman = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }

        l, r = 0, 1
        num = 0

        if len(s) == 1:
            return roman[s[l]]

        while r < len(s):
            if r == len(s) - 1:
                num += roman[s[r]]
            if roman[s[l]] >= roman[s[r]]:
                num += roman[s[l]]

            else:
                num -= roman[s[l]]

            l += 1
            r += 1

        return num
