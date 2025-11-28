def max_crossing_subarray(arr, low, mid, high):
    left_sum = -1000
    right_sum = -1000
    max_left = 0
    max_right = 0

    sum = 0
    for i in range(mid, low, -1):
        print(i)
        sum += arr[i]
        if sum > left_sum:
            left_sum = sum
            max_left = i

    sum = 0
    for i in range(mid+1, high):
        sum += arr[i]
        if sum > right_sum:
            right_sum = sum
            max_right = i

    return max_left, max_right, left_sum + right_sum


if __name__ == "__main__":
    arr = [100, 113, 110, 85, 105, 86, 63 ,81, 101, 94, 106, 101, 79, 94, 90, 97]
    changes = []

    n = len(arr)
    mid = n // 2

    print(n, mid)

    for i in range(1, n): 
        changes.append(arr[i-1] - arr[i])

    res = max_crossing_subarray(arr, 0, mid, n)
    print(res)

    


