class Solution(object):
    def removeDuplicates(self, arr):
        seen = set()


        for num in arr:
            if num not in seen:
                seen.add(num)

        
        arr[:] = sorted(seen)

        return len(arr)