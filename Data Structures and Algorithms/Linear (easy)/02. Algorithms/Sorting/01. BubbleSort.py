# in pass-one we will get the largest number at the end
# added swapped to make it efficient binary search

# best => O(n^2), average => 0(n^2), worst => 0(n^2)
# with swapped flag -> best => O(n), average => 0(n^2), worst => 0(n^2)
def bubble_sort(nums):
    n = len(nums)
    for i in range(0,n):
        swapped = False
        for j in range(0,n-i-1):
            if nums[j] > nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                swapped = True
        if not swapped: break
    return nums

nums = [850, 200, 520, 100, 430]
print("unsorted array:", nums)
bubble_sort(nums)
print("sorted array:", nums)