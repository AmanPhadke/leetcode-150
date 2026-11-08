class Solution(object):
    def uncommonFromSentences(self, s1, s2):
        res = []

        s1_hash = {}
        s2_hash = {}

        s1_words = s1.split()
        s2_words = s2.split()

        for char in s1_words:
            s1_hash[char] = s1_hash.get(char, 0) + 1

        for char in s2_words:
            s2_hash[char] = s2_hash.get(char, 0) + 1
        
        for k, v in s1_hash.items():
            if k not in s2_hash and v == 1:
                res.append(k)

        for k, v in s2_hash.items():
            if k not in s1_hash and v == 1:
                res.append(k)

        return res
  
        