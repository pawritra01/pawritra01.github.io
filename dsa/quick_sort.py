from util import generate_random_array

def quick_sort(arr):
    if len(arr) <= 1: return arr
    smaller, equal, larger = [], [], []

    pivot = arr[-1]

    for num in arr:
        if num > pivot:
            larger.append(num)
        elif num < pivot:
            smaller.append(num)
        else:
            equal.append(num)

    return quick_sort(smaller) + equal + quick_sort(larger)
    


if __name__ == "__main__":

    # arr = [1,6,3,9,5,6,2]
    arr = [1,17,2,13,4,23,7]
    n = len(arr)

    arr = quick_sort(arr)
    print(arr)

