#diyabangad
#Array-easy-9
#Union of Two Sorted Arrays
#GFG


def find_union(arr1, arr2, n, m):
    i, j = 0, 0
    union = []
    while i < n and j < m:
        if arr1[i] <= arr2[j]:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1
        else:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1
    while i < n:
        if not union or union[-1] != arr1[i]:
            union.append(arr1[i])
        i += 1
    while j < m:
        if not union or union[-1] != arr2[j]:
            union.append(arr2[j])
        j += 1
    return union

