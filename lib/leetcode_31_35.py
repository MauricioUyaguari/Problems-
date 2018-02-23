##34 Search for a Range

#Given an array of integers sorted in ascending order, find the starting and ending position of a given target value.

#Your algorithm's runtime complexity must be in the order of O(log n).

# if not found given return [-1,-1]
#first approach


nums = [5, 7, 7, 8, 8, 10]
target = 8

def search_range(nums, target):
    i = 0
    j = len(nums) - 1
    start = -1
    finish = -1
    for i in range(0,len(nums)):
        if nums[i] == target:
            start = i
            break
    while j >= 0:
        if nums[j] == target:
            finish = j
            break
        j -= 1
    print start
    print finish
    if not start and not finish:
        return [-1, -1]
    return [start, finish]

nums = [1,2,5,5,5,9]
target = 5




def search_range(nums, target):
    left_index = extreme_insertion_index(nums, target, True)
    if left_index == len(nums) or nums[left_index] != target:
        return [-1, -1]
    return [left_index, extreme_insertion_index(nums,target, False)-1]


def extreme_insertion_index(nums, target, left):
    low = 0
    high = len(nums)
    print nums
    print "low, high"
    print low, high
    while low < high:
        mid = (low + high)//2
        print "low, high, mid, nums[mid]"
        print low,high, mid, nums[mid]
        if nums[mid] > target or (left and target == nums[mid]):
            high = mid
        else:
            low = mid + 1
    return low

search_range(nums, target)
