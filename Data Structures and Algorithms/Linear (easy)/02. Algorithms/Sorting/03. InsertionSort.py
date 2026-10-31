# best => O(n), average => 0(n^2), worst => 0(n^2)
# two parts [sorted] [unsorted]

def insertion_sort(nums):
    n = len(nums)

    for i in range(1, n):
        key = nums[i]
        j = i-1

        while j>=0 and nums[j] > key:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = key
    return nums

nums = [850, 200, 520, 100, 430]
print("unsorted array:", nums)
insertion_sort(nums)
print("sorted array:", nums)