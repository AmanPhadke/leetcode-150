class Solution(object):
    def firstUniqChar(self, s):
        count = {}

        for char in s:
            count[char] = count.get(char, 0) + 1

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1
        



        