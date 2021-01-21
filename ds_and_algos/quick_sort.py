# referenceed: https://www.techiedelight.com/quicksort/

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp

def partition(a, start, end):

    pivot = a[end]
    p_index = start

    for i in range(start, end):
        if a[i] <= pivot:
            swap(a, i, p_index)
            p_index += 1

    swap(a, p_index, end)
    return p_index

def quicksort(a, start, end):

    if start >= end:
        return

    p_index = partition(a, start, end)

    quicksort(a, start, p_index-1)
    quicksort(a, p_index+1, end)

arr = [9, -3, 5, 2, 6, 8, 8, -6, 1, 3]
print(f'{arr}\n')
quicksort(arr, 0, len(arr)-1)
print(f'sorted: {arr})\n')

