#17 Letter Combinations of a Phone Number
# Given a digit string return all Combinations
# i.e  "23
#Input:Digit string "23"
#Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

def letComb(digits):
    combinations = set()
    mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                      '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
    def rec(rest_of_words, path):
        if not rest_of_words:
            combinations.add(path)
            return
        first = rest_of_words[0]
        rest = rest_of_words[1:]
        letters = mapping[first]
        for let in letters:
            rec(rest, path + let)
    rec(digits, "")
    return combinations


# 20 Valid Parathensis
#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.


v1 = "()"
v2 = "()[]{}"
n1 = "(]"
n2 = "([)]"
def isValid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        print "char"
        print char
        print "dict"
        print dict
        print "stack"
        print stack
        if char in dict.values():
            stack.append(char)
            print "stack again"
            print stack
        elif char in dict.keys():
            m = stackstac
            print "yes"
            print m
            if stack == [] or dict[char] != stack.pop():
                return False
        else:
            return False
    return stack == []
