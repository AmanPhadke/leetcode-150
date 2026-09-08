class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hashMap = {}

        for letter in magazine:
            hashMap[letter] = magazine.count(letter)


        for letter in ransomNote:
            if letter not in hashMap:
                return False
            elif hashMap[letter] == 0:
                return False
            else:
                hashMap[letter] = hashMap[letter] - 1

        return True