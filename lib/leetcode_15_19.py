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
