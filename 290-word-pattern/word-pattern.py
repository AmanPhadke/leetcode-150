class Solution(object):
    def wordPattern(self, pattern, s):
        s_list = s.split()

        if len(pattern) != len(s_list):
            return False

        charMap = {}

        for i in range(len(pattern)):
            if pattern[i] not in charMap and s_list[i] not in charMap.values():
                charMap[pattern[i]] = s_list[i]

        if not all(char in charMap for char in pattern):
            return False

        string = ' '.join(charMap[char] for char in pattern)

        if string != s:
            return False

        return True

        print(string)