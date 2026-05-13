#diyabangad
#Array - easy - 13 
#Longest Subarray with Sum K (positives only)
#Platform: GFG

def longest_subarray_sum_k(arr, k):
    left = 0
    current_sum = 0
    max_len = 0
    for right in range(len(arr)):
        current_sum += arr[right]
        while current_sum > k and left <= right:
            current_sum -= arr[left]
            left += 1
        if current_sum == k:
            max_len = max(max_len, right - left + 1)
    return max_len

