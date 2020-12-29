# MODERATE

# sort strings or numbers of equal length


def count_sort(arr, index):
    buckets = [[]]*10
    for i in range(len(arr)):
        #not sure why it was appending to every single index array
        buckets[int(arr[i][index])] = buckets[int(arr[i][index])] + [arr[i]]

    # print(buckets)
    new_arr = []
    for bucket in buckets:
        for item in bucket:
            new_arr.append(item)
    return new_arr

def add_zeros_padding(arr):
    max_len = max(len(el) for el in arr)
    for i in range(len(arr)):
        if len(arr[i]) < max_len:
            arr[i] = '0' * (max_len-len(arr[i])) + arr[i]
    return arr


def radix_sort(arr):
    # elements in arr should all have equal length (at least to start)
    arr = add_zeros_padding(arr) 
    length = len(arr[0])

    for i in range(length):
        print(i)
        arr = count_sort(arr, length-i-1)
        print(arr)
    return arr

arr = ['4230', '2235', '63', '4020', '5112']
sort_arr = radix_sort(arr)
# print(sort_arr)