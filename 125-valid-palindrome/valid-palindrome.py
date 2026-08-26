class Solution(object):
    def isPalindrome(self, s):
        clean = ''.join([char for char in s if char.isalnum()]).lower()
        
        l, r = 0, len(clean) - 1

        while l <= r:
            if clean[l] != clean[r]:
                return False
            l += 1
            r -= 1

        return True