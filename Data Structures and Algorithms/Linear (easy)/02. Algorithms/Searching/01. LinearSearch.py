# it is our first algorithm
# # sequence of steps is called an algorithm

# Linear search -> checks element one by one from start to end
# best => 0(1), average => 0(n), worst => 0(n)

def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

arr = [10,18,23,21,12,3,423,23,45,54,34,23,5,6,59,53]
target = 12

print(search(arr, target))