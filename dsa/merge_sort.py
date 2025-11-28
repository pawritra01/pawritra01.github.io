from util import generate_random_array

def merge(arr, low, mid, high):
    i = low
    j = mid+1

    m_arr = []

    while i <= mid and j <= high:
        if arr[i] < arr[j]:
            m_arr.append(arr[i])
            i += 1
        else:
            m_arr.append(arr[j])
            j += 1

    
    while i <= mid:
        m_arr.append(arr[i])
        i += 1

    while j <= high:
        m_arr.append(arr[j])
        j += 1


    k = 0
    for i in range(low, high+1):
        arr[i] = m_arr[k]
        k += 1



def merge_sort(arr, low, high):
    if low < high: 
        mid = (low + high) // 2

        merge_sort(arr, low, mid)
        merge_sort(arr, mid+1, high)

        merge(arr, low, mid, high)

if __name__ == "__main__":
    n = 10
    l = generate_random_array(n)

    print("UNSORTED: ", l)
    merge_sort(l, 0, n-1)
    print("SORTED: ", l)
