digits = [9,9,9]
stri = ""
inc_array = []

for n in digits:
    stri += str(n)

added = int(stri) + 1
restri = str(added)

for letter in restri:
    inc_array.append(int(letter))


print(inc_array)

