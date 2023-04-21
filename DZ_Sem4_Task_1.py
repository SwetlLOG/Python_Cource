
def intersection(arr1, arr2):
    res = []
    i1, i2 = 0, 0
    while True:
        if i1 >= len(arr1) or i2 >= len(arr2):
            break
        if arr1[i1] == arr2[i2]:
            res.append(arr1[i1])
            i1 += 1
            i2 += 1
        elif arr1[i1] < arr2[i2]:
            i1 += 1
        else:
            i2 += 1
    return res


print(intersection([3, 8, 6, 45, 17], [11, 6, 9, 45, 17]))
print(*sorted(set(input().split()) & set(input().split()), key=int))
