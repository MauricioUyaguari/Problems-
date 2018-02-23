#42 Trapping Rain Water
#Given n non-negative nintegers representing an elevation map where the width of each bar is 1, compute how much water it is able
#to trap after raining




nums = [0,1,0,2,1,0,1,3,2,1,2,1]
def trap(nums):
    left = 0
    right = len(nums) - 1
    result = 0
    left_max = 0
    right_max = 0
    while left < right:
        print "left, right"
        print left, right
        print "left_max"
        print left_max
        print "right_max"
        print right_max
        if nums[left] < nums[right]:
            if nums[left] >= left_max:
                left_max = nums[left]
            else:
                result += (left_max - nums[left])
                print "result added through left"
                print result
            left += 1
        else:
            if nums[right] >= right_max:
                right_max = nums[right]
            else:
                result += (right_max - nums[right])
                print "result added through right"
                print result
            right -= 1
    return result
trap(nums)






#46 permutations
a = [1,2,3]
a1 = [1,2,3,4]


#solutions






def per(arr):
    result = []
    for i in range(0,len(arr)):
        new_array = arr[0:i] + arr[i+1:len(arr)]
        insert = arr[i]
        for j in range(0, len(new_array) + 1 ):
            if True:
                print new_array
                left = new_array[0:j]
                print left
                right = new_array[j:len(new_array)]
                perm = left + [insert] + right
                result.append(perm)
    new_result = []
    for el in result:
        if not el in new_result:
            new_result.append(el)
    return new_result




#46 permuations


def per2(arr):
    if len(arr) == 0:
        return []
    elif len(arr) == 1:
        return [arr]
    else:
        l = []
        for i in range(len(arr)):
            element = arr[i]
            print "element"
            print element
            notelement = arr[:i] + arr[i + 1:]
            print "notelement"
            print notelement
            for p in perm1(notelement):
                print "p"
                print p
                l.append([element] + p)
                print "result"
                print l
        return l


def perm1(lst):
	if len(lst) == 0:
		return []
	elif len(lst) == 1:
		return [lst]
	else:
		l = []
		for i in range(len(lst)):
			x = lst[i]
			xs = lst[:i] + lst[i+1:]
			for p in perm1(xs):
				l.append([x] + p)
		return l

# sal
#sal y color
