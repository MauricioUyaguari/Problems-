def secondsmallest(array):
    if len(array) < 2:
        return null
    else:
        smallest = min(array)
        array.remove(smallest)
        return min(array)





def second_smallest(array):
    if len(array) < 2:
        return null
    smallest = min(array)
    array.remove(smallest)
    return min(array)

# 2. IsAnagram


def is_anagram(s,t):
    count = {}
    for l in s:
        if l is not in s:
            count[l] = 1
        else:
            count[l] += 1
    for e in t:
        if e is not in s:
            return False
        else:
            count[e] -= 1
    for key in count:
        if count[key] != 0:
            return False
    return True


def is_anagram(s, t):
    count = {}
    for let in s:
        if let not in count:
            count[let] = 1
        else:
            count[let] += 1
    for let in t:
        if let not in count:
            return False
        else:
            count[let] -= 1
    for key in count:
        if count[key] != 0:
            return False
    return True



# 3. Count unique substring of length k

def unique_substrings_length(k):
    i = 0
    j = 0




def reverse_string(s):
    result = ""
    for let in s:
        result = let + result
    return result




#you want to return all indixes where the two numbers sum to k

def sum_to_k(a,target):
    count = {}
    result = []
    for i in range(0,len(a)):
        complement = target - a[i]
        if complement not in count:
            count[complement] = i
        else:
            result.append([count[complement], i])
    return result


def sum(array, target):
    i = 0
    j = len(array) - 1
    while i != j:
        sum = array[i] + array[j]
        if sum == target:
            result = [i + 1, j + 1]
        elif sum < target:
            i += 1
        else:
            j -= 1
    if len(result) > 0:
        return result
    else:
        return null





def find_target(root, target):
    if root.val == null:
        return null
    count = {}
    complement = target - root.val
    if root.val in count:
        return True
    else:
        count[complement] = True
        find_target(root.left, target)
        find_target(root.right, target)


def removeDuplicates(nums):
    count = set()
    i = 0
    while i < len(nums):
        if nums[i] not in count:
            count.add(nums[i])
            i += 1
        else:
            nums.pop(i)
    return nums




def bsearch(nums, target):
    if len(nums) < 1:
        return 1
    mid = len(nums)/2
    left = nums[0:mid]
    right = nums[mid:len(nums)-1]
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        if len(right) == 1:
            return mid + bsearch(right, target) + 1
        else:
            return mid + bsearch(right, target)
    else:
        return bsearch(left, target)


test  = ["a"]


def l(strs):
    if len(strs) < 1 or len(strs[0]) < 1:
        return ""
    shortest_word = strs[0]
    for word in strs:
        if len(word) < len(shortest_word):
            shortest_word = word
    for i in range(0, len(shortest_word) - 1):
        temp = shortest_word[0:i]
        for word in strs:
            if temp != word[0:i]:
                return temp
    return shortest_word




def l(strs):
    if not strs:
        return ""

    for i, letter_group in enumerate(zip(*strs)):
        print i
        print letter_group
        if len(set(letter_group)) > 1:
            return strs[0][:i]
    else:
        return min(strs)



#shortest to equal
#[1,2,3,4], 6

def short(arr, target):
    if len(arr) < 1:
        return -1
    i = 0
    j = 1
    result = -1
    while i < len(arr) and j < len(arr) + 1:
        print arr[i:j]
        if sum(arr[i:j]) >= target:
            if result == -1:
                result = j - i
                i += 1
            else:
                result = min(result, j - i)
                i += 1
        elif j == len(arr):
            i += 1
        else:
            j += 1
    return result
