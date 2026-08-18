class Solution(object):
    def groupAnagrams(self, strs):
        sub = {}

        for string in strs:
            key = ''.join(sorted(string))

            if key not in sub:
                sub[key] = []

            sub[key].append(string)

        return list(sub.values())

