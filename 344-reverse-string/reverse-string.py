class Solution(object):
    def reverseString(self, s):
        # s[:] = [s[i] for i in range(len(s)-1,-1,-1)]

        l = 0
        r = len(s) -1

        while l < r:
            s[l], s[r] = s[r], s[l]

            l +=1
            r -= 1


        