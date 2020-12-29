# EASY/MODERATE
import random
# help from: https://www.geeksforgeeks.org/merge-sort/

# def merge(arr1, arr2):
    
#     i = 0; j = 0
#     result = []
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             result.append(arr1[i])
#             i += 1
#         else:
#             result.append(arr2[j])
#             j += 1
    
#     while i < len(arr1):
#        result.append(arr1[i]) 
#        i += 1
#     while j < len(arr2):
#        result.append(arr2[j]) 
#        j += 1

#     return result



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2

        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        # merge part
        # if using another function, use indexes like l and h
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1; k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1; k += 1

def is_sorted(arr):
    if len(arr) <= 1:
        return True
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False
    return True

def create_random_arrays(num_arrays):
    all_arrays = []
    for _ in range(num_arrays):
        random_length = random.randint(2, 20)
        arr = []
        for _ in range(random_length):
            random_num = random.randint(0, 100)
            arr.append(random_num)
        all_arrays.append(arr)
    
    return all_arrays
        
def print_arr_info(all_arrays):
    avg_len = sum(len(a) for a in all_arrays)/len(all_arrays)
    print(f'avg length of arrays: {avg_len}')
    for a in all_arrays:
        print(a)
    
def main():
    all_arrays = create_random_arrays(20)
    print_arr_info(all_arrays)
    for arr in all_arrays:
        merge_sort(arr)
        assert is_sorted(arr)==True 

main()
# merged = merge([1,3,5], [2,4,6])
# print(merged)

# if __name__ == __main__:
#     r