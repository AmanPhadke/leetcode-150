class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = []
        i, j = 0, 0

        for num in nums1:
            if i < m:
                res.append(num)
                i += 1
            else:
                break

        for num in nums2:
            if j < n:
                res.append(num)
                j += 1
            else:
                break

        nums1[:] = sorted(res)
            