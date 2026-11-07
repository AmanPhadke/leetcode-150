class Solution(object):
    def reverseVowels(self, s):
        vowels = 'aeiouAEIOU'
        sl = []

        l, r = 0, len(s) - 1

        for char in s:
            sl.append(char)

        while l < r:
            if sl[l] in vowels and sl[r] in vowels:
                sl[l], sl[r] = sl[r], sl[l]
                l += 1
                r -= 1

            elif sl[l] not in vowels and sl[r] in vowels:
                l += 1

            elif sl[r] not in vowels and sl[l] in vowels:
                r -= 1

            else:
                l += 1
                r -= 1

        return ''.join(char for char in sl)

            
        