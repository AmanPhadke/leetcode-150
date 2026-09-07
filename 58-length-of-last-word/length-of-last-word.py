class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        count = 0
        l = -1

        if ' ' not in s:
            return len(s)

        while s[l] != ' ':
            count += 1
            l -= 1

        return count