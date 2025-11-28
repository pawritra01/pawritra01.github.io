from util import generate_random_array

def get_digit(num, n):
    return num // pow(10, n - 1) % 10

def radix_sort(arr, max_digits=4):
    buckets = [[], [], [], [], [], [], [], [], [], []]

    for i in range(1, max_digits + 1):
        for num in arr:
            dig = get_digit(num, i)
            buckets[dig].append(num)
    
        new_arr = []
        for idx, val in enumerate(buckets):
            new_arr.extend(val)
            buckets[idx] = []

        arr = new_arr

    return arr




if __name__ == "__main__":
    arr = generate_random_array(20)

    arr = radix_sort(arr, 4)
    print(arr)
    
    
