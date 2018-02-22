## 11 Container with the most water

nums = [1, 8, 6, 2, 5, 4, 8, 3, 7]

def maxArea(nums):
    i = 0
    j = len(nums) - 1
    max_area = 0
    while i != j:
        width = j - i
        height = min(nums[i], nums[j])
        print "width, hight"
        print width, height
        max_area = max(max_area, width * height)
        if nums[j] > nums[i]:
            i += 1
        else:
            j -=1
    return max_area

maxArea(nums)


## 12 Integer to Roman

#Given an integer, convert it to a roman numeral.

#Input is guaranteed to be within the range from 1 to 3999.

def intToRoman(num):
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    s_thousands = thousands[num / 1000]
    s_hundreds = hundreds[(num / 100) % 10]
    s_tens = tens[(num / 10) % 10]
    s_ones = ones[num % 10 ]
    result = s_thousands + s_hundreds + s_tens + s_ones
    return result

# 13 Roman to Integer

rome = "DCXXI"
output = 621

def romanToInt(s):
    roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
    z = 0
    for i in range(0, len(s) - 1):
        print "i, s[i]"
        print i, s[i]
        print "z"
        print z
        if roman[s[i]] < roman[s[i+1]]:
            z -= roman[s[i]]
        else:
            z += roman[s[i]]
    return z + roman[s[-1]]



## 15:  3Sum LeetCode
nums = [-1,0,1,2,-1,-4]
#shoudl return
answer = [[-1,0,1], [-1,-1,2]]

def threeSum(nums):
    result = []
    nums.sort()
    #n(log(n))
    for i in range(0, len(nums) - 2):
        print "i"
        print i
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = len(nums) - 1
        print "l,r"
        print l,r
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            print "s"
            print s
            if s < 0:
                l += 1
            elif s > 0:
                r -= 1
            else:
                result.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
    return result

threeSum(nums)
