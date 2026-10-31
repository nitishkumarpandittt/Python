# in pass-one we will get the smallest number at the start
# best => O(n^2), average => 0(n^2), worst => 0(n^2)

def selection_sort(nums):
    n = len(nums)

    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

nums = [850, 200, 520, 100, 430]
print("unsorted array:", nums)
selection_sort(nums)
print("sorted array:", nums)