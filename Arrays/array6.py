nums = [1,3,5,6]
#new = [1,2,3,4,5,6]
new  = []
target = 4

if target in nums:
    print(int(nums.index(target)))
else:
    for i in range(min(nums), max(nums)+1):
        new.append(i)
    print(new)

    for i in new:
        if (i == target):
            print(new.index(i))
            break
        elif (i != target):
            print(len(nums))
            break
        else:
            new.pop(i)
        


