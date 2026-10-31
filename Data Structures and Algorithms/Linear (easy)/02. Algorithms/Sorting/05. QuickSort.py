# best => O(nlogn), average => 0(nlogn), worst => 0(n^2)

def quick_sort(nums):
    if len(nums) <= 1:
        return nums

    pivot = nums[-1]
    smaller = []
    greator = []

    for n in nums[:-1]: # excluding pivot
        if n <= pivot:
            smaller.append(n)
        else:
            greator.append(n)
    nums[:] = quick_sort(smaller) + [pivot] + quick_sort(greator)
    return nums

nums = [850, 200, 520, 100, 430]
print("unsorted array:", nums)
quick_sort(nums)
print("sorted array:", nums)