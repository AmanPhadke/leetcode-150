class Solution(object):
    def sortPeople(self, names, heights):
        heightMap = {}

        for i in range(len(heights)):
            heightMap[heights[i]] = names[i]

        return [heightMap[key] for key in sorted(heightMap, reverse=True)]
        