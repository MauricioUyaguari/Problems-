## 6 ZigZag Conversion


def convert(string, n_rows)
  string_letters = string.chars
  let_count = string_letters.length
  result_table = Array.new(n_rows, "")

  i = 0
  while i < let_count
    idx = 0
    while idx < n_rows && i < let_count

      result_table[idx] += string_letters[i]
      i += 1
      idx += 1
    end

    idx -= 2
    while idx > 0 && i < let_count
      result_table[idx] += string_letters[i]
      idx -= 1
      i += 1
    end
  end
  return result_table.join("")
end




## 7  Reverse an Integer
# Given a 32-bit signed integer, reverse digits of an integer.


def my_reverse(x)
    neg = false
    neg = true if x < 0

    x = x.abs.to_s.split("")

    result = ""
    x.each do |num|
        result = num.to_s + result
    end
    result = result.to_i
    return 0 if result > (2 ** 32) / 2
    if neg
        return result * -1
    else
        return result
    end

end


# string to integer



def my_atoi(str)
  str = str.strip
  chars = str.split("")
  return 0 if chars.empty?

  if chars.include?(" ")
    idx = chars.find_index(" ")
    chars = chars[0...idx]
  end

  sign = (chars[0] == "-") ? -1 : 1
  if chars[0] == "-" || chars[0] == "+"
    chars.delete_at(0)
  end
  ret = 0
  i = 0
  digits = {}
  (0..9).to_a.each {|num| digits[num.to_s] = num}
  while i < chars.length && digits.key?(chars[i])
    add = digits[chars[i]]
    ret = ret * 10 + add
    i += 1
  end
    return (2 ** 31 - 1) if ret > 2 ** 31 - 1 && sign == 1
    return (2 ** 31) * sign if ret > 2 ** 31 && sign == -1
  return ret * sign
end






##9 num is_palindrome




def is_palindrome(num)
  return true if num == 0
  return false if num % 10 == 0 || num < 0
  # our goal for this problem is to revert half of the numbers
  #then check if that half equals the begining

  # for example if we take the number 1221
  # we want to compare the first two digits to the last two digits
  # hence we want to compare 12 to 21 reversed
  revert = 0
  while num > revert
    add = num % 10
    revert = revert * 10 + add
    num = num / 10
  end


  return revert == num || num == revert/ 10

end
