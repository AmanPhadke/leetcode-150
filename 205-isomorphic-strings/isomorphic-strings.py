class Solution(object):
    def isIsomorphic(self, s, t):
        hashMap = {}
        revMap = {}
        temp = ''

        for i in range(len(s)):
            if (s[i] in hashMap):
                if (hashMap[s[i]] != t[i]):
                    return False

            else:
                if t[i] in revMap:
                    return False

            hashMap[s[i]] = t[i]
            revMap[t[i]] = s[i]

        return True