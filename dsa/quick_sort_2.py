from util import generate_random_array


def partition(arr, low, high):
    pivot = arr[low]
    i, j = low, high

    while i < j:
        while pivot > arr[i]: i += 1
        while pivot < arr[j]: j -= 1

        arr[i], arr[j] = arr[j], arr[i]

        if arr[i] == arr[j]: j -= 1

    return i


# def partition(arr, low, high):
#     pivot = arr[low]
#     i, j = low - 1, high + 1
#
#     while True:
#         while True:
#             i += 1
#             if arr[i] >= pivot:
#                 break
#
#         while True:
#             j -= 1
#             if arr[j] <= pivot:
#                 break
#
#         if i >= j:
#             return j
#
#         arr[i], arr[j] = arr[j], arr[i]



def quick_sort(arr, low, high):
    if low < high:
        idx = partition(arr, low, high)

        quick_sort(arr, low, idx)
        quick_sort(arr, idx + 1, high)


if __name__ == "__main__":
    arr = generate_random_array(7)
    n = len(arr)

    print(arr)
    quick_sort(arr, 0, n - 1)
    print(arr)
