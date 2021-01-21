
# vanilla binary search
# make sure you are returning each call, not just calling it
def binary_search(arr, l, h, target):
    if l <= h:
        mid = (l+h)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binary_search(arr, l, mid-1, target)
        else: 
            return binary_search(arr, mid+1, h, target)
    else:
        return -1



print("binary search:")
arr1 = [1,2,3,5,6,33,366]
for i in (3,366,400, 1,-3):
    print(f'searching for value: {i}')
    bin_search = binary_search(arr1, 0, len(arr1)-1, i)
    if bin_search == -1:
        print("value not found")
    else:
        print(f"value found at index {bin_search}")









# Peak Finding
def find_peak(nums, l, r):
    mid = (r+l)//2

    if l == r:
        return l

    if nums[mid] < nums[mid-1]:
        return find_peak(nums, l, mid-1)

    elif nums[mid] < nums[mid+1]:
        return find_peak(nums, mid+1, r)

    return mid

tests = [
    [[1,4,6,5,3,4], [6]],
    [[1,3,8,9,10], [10]],
    [[8,4,6,5,3,9], [8, 6, 9]],
    [[1,4], [4]],
    [[1], [1]],
    [[4,3,1], [4]],
    [[2,6,1], [6]]
]

for entry in tests:
    print(entry)
    test_arr, corr_res = entry[0], entry[1]
    peak_index = find_peak(test_arr, 0, len(test_arr)-1) 
    assert test_arr[peak_index] in corr_res
