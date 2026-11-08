class Solution(object):
    def mergeSimilarItems(self, items1, items2):
        res = []
        charMap = {}
        for value, weight in items1 + items2:
            charMap[value] = charMap.get(value, 0) + weight

        return [[key, charMap[key]] for key in sorted(charMap)]
