class Solution(object):
    def groupAnagrams(self, strs):
        res = []
        group = {}

        for word in strs:
            word_set = tuple(sorted(word))
            group[word_set] = group.get(word_set, []) + [word]


        for key, value in group.items():
            res.append(value)

        return sorted(res)
