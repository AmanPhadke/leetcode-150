nums = [1,2,2,3,4,4,5]
val = 4

nums[:] = [x for x in nums if x != val]


print(len(nums))