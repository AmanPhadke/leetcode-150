class Solution(object):
    def rotate(self, arr, d):

        d = d % len(arr)

        def reverse(l, r):
            while l < r:
                arr[l] , arr[r] = arr[r] , arr[l]
                l, r = l + 1, r - 1

            return arr

        l, r = 0, len(arr) - 1

        reverse(l, r)

        l, r = 0, d - 1
        reverse(l, r)

        l, r = d, len(arr) - 1
        reverse(l, r)