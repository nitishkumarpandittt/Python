# list should be sorted for binary search

def search(nums, target):
    left = 0
    right = len(nums) - 1
    while(left <= right):
        mid = (left + right) >> 1

        if nums[mid] == target:
            return mid

        elif nums[mid] > target:
            right -= 1
        else: left += 1
    return -1

arr = [3, 5, 6, 10, 12, 18, 21, 23, 23, 23, 34, 45, 53, 54, 59, 423]
target = 12

print(search(arr, target))