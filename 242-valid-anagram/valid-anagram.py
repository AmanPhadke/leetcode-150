class Solution(object):
    def isAnagram(self, s, t):
        seen_s = set()
        seen_t = set()
        count_s = 0
        count_t = 0

        if len(s) != len(t):
            return False

        for letter in set(s):
            if s.count(letter) != t.count(letter):
                return False
        
        return True

        


        
