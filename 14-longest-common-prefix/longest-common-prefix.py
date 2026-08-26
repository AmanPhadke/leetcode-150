class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ''
        seen = strs[0]
        min_length = float('inf')

        for char in strs:
            min_length = min(min_length, len(char))

        for i in range(min_length):
            for s in strs:
                if s[i] != seen[i]:
                    return res
                
            res += seen[i]
    
        return res

        