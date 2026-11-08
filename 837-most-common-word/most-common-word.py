import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        hashMap = {}

        paragraph = re.sub(r'[^\w\s]', ' ', paragraph).lower()
        words = paragraph.split()

        for word in words:
            if word not in banned:
                hashMap[word] = hashMap.get(word, 0) + 1
        
        return max(hashMap, key=hashMap.get)
