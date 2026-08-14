class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        count = 0
        res = []
        for i in range(n+1):
            current = i
            bits = ''
            while current > 0:
                bit = current % 2
                current //= 2
                if bit == 1:
                    count += 1

            res.append(count)
            count = 0

        return res