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
