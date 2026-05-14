#diyabangad
#Array - easy - 1 
#Largest Element in an array
#GFG 
def largest(arr, n):
    maxi = arr[0]
    for i in range(1, n):
        if arr[i] > maxi:
            maxi = arr[i]
    return maxi
