class Solution(object):
    def isAnagram(self, s, t):
        if len(s) == len(t):
            for letter in t:
                if (letter in s):
                    if t.count(letter) == s.count(letter):
                        continue
                    else:
                        return False
                else:
                    return False
        else:
            return False

        return True