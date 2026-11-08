class Solution(object):
    def isIsomorphic(self, s, t):
        charMap = {}
        temp = ''

        for i in range(len(s)):
            if s[i] not in charMap and t[i] not in charMap.values():
                charMap[s[i]] = t[i]

        for char in s:
            if char not in charMap:
                return False
    
            temp += charMap[char]

        if temp != t:
            return False

        return True
        