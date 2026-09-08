class Solution(object):
    def reverseString(self, s):
        s[:] = [s[i] for i in range(len(s)-1,-1,-1)]