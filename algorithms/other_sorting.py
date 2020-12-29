# EASY

# simpler but less efficient sorting algorithms
# Selection, insertion, and bubble sort 
# See Radix & quick in algorithms and heap & merge in data_structures

# Selection ((n^2))
# Insertion ((n^2))
# Bubble ((n^2))
# Merge ((O(lgn)))
# Quick ((O(lgn)))
# Radix (O(k*n))


# Selection sort
def selection_sort(arr):
    for i in range(len(arr)-1):
        temp = arr[i]
        minimum = arr[i]
        min_j = i
        for j in range(i+1, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                min_j = j
        arr[i] = arr[min_j]
        arr[min_j] = temp
    return arr
        

# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(0, i):
            if arr[i] < arr[j]:
                # swap
                temp = arr[i]
                # shift
                k = i
                while(k > j):
                    arr[k] = arr[k-1]
                    k -= 1
                arr[j] = temp
    return arr


# Bubble sort
def bubble_sort(arr):
    k = len(arr)
    for _ in range(0, len(arr)-1):
        j = 1
        while (j < k):
            if arr[j] < arr[j-1]:
                # swap
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
                print(arr)
            j += 1
        k -= 1
    return arr

arr = [2,4,1,6,77,24]
# selection = selection_sort(arr)
# insertion = insertion_sort(arr)
# bubble = bubble_sort(arr)
# print(insertion)