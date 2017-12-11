a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 11, 15]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

if len(b) > len(a):
    overlaps = [num for num in b if num in a]
else:
    overlaps = [num for num in a if num in b]

print(set(overlaps))
