#diyabangad
#Array - easy - 5
#Left Rotate an Array by One Place
#GFG

def rotate_by_one(arr, n):
    temp = arr[0]          # store first element
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp      # place first element at end
    return arr
