## 11 Container with the most water




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
