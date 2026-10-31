# divivide and conquer (solve) and combine
# best => O(nlogn), average => 0(nlogn), worst => 0(nlogn)

def combine_helper(left, right):
    finalList = []
    left_ptr = 0
    right_ptr = 0

    while left_ptr < len(left) and right_ptr < len(right):
        left_element = left[left_ptr]
        right_element = right[right_ptr]

        if left_element <= right_element:
            finalList.append(left[left_ptr])
            left_ptr += 1
        else:
            finalList.append(right[right_ptr])
            right_ptr += 1

    while left_ptr < len(left):
        finalList.append(left[left_ptr])
        left_ptr += 1

    while right_ptr < len(right):
        finalList.append(right[right_ptr])
        right_ptr += 1

    return finalList

def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    mid = len(nums) // 2
    left = nums[:mid]
    right = nums[mid:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    # sorted_result = combine_helper(sorted_left, sorted_right)

    # in-place 
    nums[:] = combine_helper(sorted_left, sorted_right)

    return nums

#           for not in-place
# nums = [850, 200, 520, 100, 430]
# print("unsorted array:", nums)
# nums = merge_sort(nums)
# print("sorted array:", nums)

nums = [850, 200, 520, 100, 430]
print("unsorted array:", nums)
merge_sort(nums)
print("sorted array:", nums)
