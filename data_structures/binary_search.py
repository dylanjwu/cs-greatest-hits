# EASY

#Peak Finding
def binary_search(nums, l, r):
    mid = (r+l)//2

    if l == r:
        return l

    if nums[mid] < nums[mid-1]:
        return binary_search(nums, l, mid-1)

    elif nums[mid] < nums[mid+1]:
        return binary_search(nums, mid+1, r)

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
    peak_index = binary_search(test_arr, 0, len(test_arr)-1) 
    assert test_arr[peak_index] in corr_res
