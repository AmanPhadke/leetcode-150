class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count_mag = {}
        count_ransom = {}

        for char in magazine:
            count_mag[char] = count_mag.get(char, 0) + 1

        for char in ransomNote:
            count_ransom[char] = count_ransom.get(char, 0) + 1

        for k,v in count_ransom.items():
            if k not in magazine:
                return False

            elif v > count_mag[k]:
                return False 

        return True
