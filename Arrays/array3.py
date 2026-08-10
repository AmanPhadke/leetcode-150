arr = [5,1]

sorted_arr = sorted(arr)
new_arr = []
missing = []

for i in range(sorted_arr[0], sorted_arr[-1]+1):
    new_arr.append(i)

for j in new_arr:
    if j not in sorted_arr:
        missing.append(j)

print(missing)