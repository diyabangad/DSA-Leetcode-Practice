#diyabangad
#Array - easy - 2
#Second Largest Element in an Array
#GFG

def print_second_largest(arr, n):
    largest = -1
    second = -1
    for i in range(n):
        if arr[i] > largest:
            second = largest
            largest = arr[i]
        elif arr[i] > second and arr[i] != largest:
            second = arr[i]
    return second
