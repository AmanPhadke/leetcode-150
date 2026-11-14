class Solution(object):
    def minimumAbsDifference(self, arr):
        arr = sorted(arr)
        res = []
        min_abs = float('inf')

        for i in range(1, len(arr)):
            min_abs = min(arr[i] - arr[i-1], min_abs)

        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == min_abs:
                res.append([arr[i-1], arr[i]])


        return res

        