class Solution(object):
    def groupAnagrams(self, strs):
        group = {}

        for word in strs:
            word_set = tuple(sorted(word))
            group[word_set] = group.get(word_set, []) + [word]

        return list(group.values())
