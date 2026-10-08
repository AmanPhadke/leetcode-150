class Solution(object):
    def moveZeroes(self, arr):
        zero = 0
        temp = []

        for i in range(len(arr)):
            if arr[i] != 0:
                temp.append(arr[i])
            
            else:
                zero += 1

        arr[:] = temp + [0]*zero
            
        return arr
        