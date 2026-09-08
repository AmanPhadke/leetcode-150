class Solution(object):
    def firstUniqChar(self, s):
        seen = set()
        for i in range(len(s)):
            if s[i] not in seen:
                if s.count(s[i]) < 2:
                    return i
                seen.add(s[i])

        return -1