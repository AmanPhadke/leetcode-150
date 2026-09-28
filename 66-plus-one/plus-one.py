class Solution(object):
    def plusOne(self, arr):
        for i in range(len(arr)-1, -1, -1):
            if arr[i] < 9:
                arr[i] += 1
                return arr
            arr[i] = 0

        return [1] + arr
        