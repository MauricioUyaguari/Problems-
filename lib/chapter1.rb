def is_unique?(string)
  string.each_char.with_object({}) do |char, hash_table|
    if hash_table[char]
      return false
    else
      hash_table[char] = true
    end
  end

  true
end



def check_permutation_solution2(s1="", s2="")
	return false if s1.length != s2.length
	letters = Array.new(128, 0)

	s1.chars{ |char| letters[char.ord] += 1 }
	s2.chars{|char| return false if (letters[char.ord] -= 1) < 0 }
	true
end




def pal(str)
  count = Hash.new(0)
  str.each_char do |char|
    if count[char] == 1
      count[char] = 0
    else
      count[char] = 1
    end
  end
  sum = count.values.reduce(:+)
  return true if str.length.even? && sum == 0
  return true if str.length.odd? && sum == 1
  false
end
