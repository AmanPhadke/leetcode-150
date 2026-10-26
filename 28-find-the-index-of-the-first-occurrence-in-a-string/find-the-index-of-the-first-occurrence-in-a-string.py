class Solution(object):
    def strStr(self, haystack, needle):
        l, r = 0, len(needle)

        if haystack == needle:
            return 0


        while r <= len(haystack):
            if haystack[l:r] == needle:
                return l

            l += 1
            r += 1

        return -1
        