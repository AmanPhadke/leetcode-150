arr = [3,5,4,1,9, 10, 15, 12, 11]

def findMinMax(arr):
    sorted_arr = sorted(arr)
    min = sorted_arr[0]
    max = sorted_arr[-1]
    return min, max

min, max = findMinMax(arr)
print(min, max)
