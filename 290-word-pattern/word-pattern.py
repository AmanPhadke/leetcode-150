class Solution(object):
    def wordPattern(self, t, s):
        hashMap = {}
        rev = {}

        words = s.split(' ')


        if len(words) != len(t):
            return False

        for i in range(0, len(words)):
            
            if words[i] in hashMap:
                if hashMap[words[i]] != t[i]:
                    return False

            else:
                if t[i] in rev:
                    return False

            hashMap[words[i]] = t[i]
            rev[t[i]] = words[i]

        return True
