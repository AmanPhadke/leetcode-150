class Solution(object):
    def hammingWeight(self, n):
        count = 0

        current = n

        while (current > 0):
            rem = current % 2
            current = current // 2

            if rem == 1:
                count += 1


        return (count)
        