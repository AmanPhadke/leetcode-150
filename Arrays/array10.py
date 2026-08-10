numRows = 5

i = 0

while i < numRows - 1:
    if nums[i] <= nums[i+1]:
        nums[i+1] = nums[i] + nums[i+1]
        i += 1

    else:
        nums[i+1] = nums[i] - nums[i+1]
        i +=1


print(nums)

