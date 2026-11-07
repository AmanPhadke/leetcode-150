class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count_ransom = {}

        for char in magazine:
            count_ransom[char] = count_ransom.get(char, 0) + 1


        for char in ransomNote:
            if char not in count_ransom:
                return False
            
            elif count_ransom[char] < ransomNote.count(char):
                return False

        return True