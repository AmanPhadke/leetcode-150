class Solution(object):
    def hammingWeight(self, n):
        binary = (bin(n)[2:])
        count = 0

        for i in binary:
            if i == '1':
                count += 1

        return count
        
        