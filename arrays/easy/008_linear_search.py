#diyabangad
#Array - easy - 8
#Linear Search
#GFG


def linear_search(arr, n, key):
    for i in range(n):
        if arr[i] == key:
            return i   # return index if found
    return -1 
