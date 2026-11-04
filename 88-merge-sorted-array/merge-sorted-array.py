class Solution(object):
    def merge(self, nums1, m, nums2, n):
        temp = []
        for i in range(m):
            temp.append(nums1[i])

        for j in range(n):
            temp.append(nums2[j])

        nums1[:] = sorted(temp)

        

        
