require 'byebug'

# probem 1


#problem 2
def add_two_numbers(l1, l2)
    carry = 0
    current1 = l1
    current2 = l2
    result = nil
    while (current1 != nil or current2 != nil) or carry != 0
        val1 = (current1 == nil) ? 0 : current1.val
        val2 = (current2 == nil) ? 0 : current2.val
        sum = val1 + val2 + carry
        carry = sum / 10
        append = sum % 10

        if result == nil
            result = ListNode.new(append)
            first = result
        else

            temp = ListNode.new(append)
            result.next = temp
            result = result.next
        end

        current1 = current1.next if current1 != nil
        current2 = current2.next if current2 != nil
    end


    return first
end

# problem 2 other method
def add_two_numbers2(l1, l2)
    current_node_1 = l1
    num1 = []
    while current_node_1 != nil
        num1.unshift(current_node_1.val)
        current_node_1 = current_node_1.next
    end

    current_node_2 = l2
    num2 = []
    while current_node_2 != nil
      num2.unshift(current_node_2.val)
      current_node_2 = current_node_2.next
    end

    total = num1.join("").to_i + num2.join("").to_i
    total = total.to_s.split("").map{|el| el.to_i}

    resultnode = ListNode.new(total.pop())

    current = resultnode
    while !total.empty?
        current.next = ListNode.new(total.pop())
        current = current.next
    end

    return resultnode

end



## problem 3



#my solution. this failed for one/ 983
def length_of_longest_substring(s)

    i = 0
    max = ""
    while i < s.length
        letters = {}
        j = i
        until letters.key?(s[j]) || j >= s.length
            substring = s[i..j]
            if substring.length > max.length
                max = substring
            end
            letters[s[j]] = j
            j += 1
        end

        if letters.key?(s[j])
            i = letters[s[j]] + 1
        else
            i = i + 1
        end
    end
    return max.length
end



# commented solution

def solution_length_of_longest_substring(s)
    count = Hash.new(0)
    len = first = last = 0
    while last < s.length do
        if count[s[last]] == 0
            len = [len, last - first + 1].max
            puts "max"
            print [len, last - first + 1]
            puts ""
            puts "s[last]"
            puts s[last]
            puts "count[s[sllast]]"
            print count[s[last]]
            count[s[last]] += 1
            last += 1
        else
            puts "else"
            count[s[first]] -= 1
            first += 1
        end
        puts count
        puts "first"
        puts first
        puts "last"
        puts last

    end
    len
end


def length_of_longest_substring(s)
    count = Hash.new(0)
    max = 0
    i = 0
    j = 0

    # you are going to have a silding window with i and j moving
    # they will move depending on when they see a new UNIQUE string

    while j < s.length do
        if count[s[j]] == 0
            # they have not seen this letter. can keep adding to the substring
            max = [j - i + 1, max].max
            #this max will be either be the max(j - i + 1) that they have seen before or the current j - i + 1 depending
            #on which one is bigger
            count[s[j]] += 1
            # add to key
            j += 1
            #increase j
        else
            #this is when the new letter to be added is already in the substring.
            # to start a new substring you substract 1 until you have a substring again with all unique letters
            count[s[i]] -= 1
            i += 1
        end
    end


    return max


    #this while loop will end when you finish traversing through the string
end


## Problem 4 find the median of two sorted Arrays
#test cases

a = [1,3,8,9,15]
b = [7,11,18,19,21,25]
def find_median_sorted_arrays(a,b)
  m, n = a.length, b.length
  if m > n
      a, b, m, n = b, a, n, m
  end
  # a is smaller array with length m
  #b is bigger array with length n
  imin = 0
  imax = m
  # you want to be doing the binary search on the smaller array hence the largest one is
  #m
  # this is the half length of both m and n
  half_length = (m + n + 1) / 2
  while imin <= imax
    i = (imin + imax) / 2
    j = half_length - i
    puts "imax"
    puts imax
    puts "imin"
    puts imin
    puts "i"
    puts i
    puts a[i]
    puts "j"
    puts j
    puts b[j]

    puts "numbers compared a"
    puts a[i], a[i - 1]
    puts "numbers compared b"
    puts b[j], b[j-1]
    if i < m && b[j-1] > a[i]
      #i is too small, must increase it

      puts "i is too small"

      imin = i + 1
    elsif i > 0 && a[i-1] > b[j]
      # i is too big must decrease it
      puts "i is too big"
      imax = i -  1
    else
      if i == 0
        max_of_left = b[j-1]
      elsif j == 0
        max_of_left = a[i-1]
      else
        max_of_left = [a[i-1], b[j-1]].max
      end

      if (m + n ) % 2 == 1
        return max_of_left
      end

      if i == m
        min_of_right = b[j]
      elsif j == n
        min_of_right = a[i]
      else
        min_of_right = [a[i], b[j]].min
      end
      puts max_of_left
      puts min_of_right
      return (max_of_left + min_of_right)/ 2.0
    end
    false
  end

end

median(a,b)







## problem 5

def longest_palindrome(str)
    start = 0
    finish = 0

    idx = 0
    while idx < str.length
        oddlen = expandCenter(str, idx, idx)
        evenlen = expandCenter(str, idx, idx + 1)
        len = [oddlen, evenlen].max

        puts "idx"
        puts idx
        puts "odd, even"
        puts "#{oddlen}, #{evenlen}"
        puts "len"
        puts len
        if len > finish - start
            start = idx - ((len - 1) / 2)
            finish = idx + (len/2)
        end
        puts "start"
        puts start
        puts "finish"
        puts finish
        puts "substring"
        puts str[start..finish]
        idx += 1
    end

    return str[start..finish]
end

def expandCenter(str, left, right)
    while left >= 0 && right < str.length && str[left] == str[right]
        left -= 1
        right += 1
    end
    return right - left - 1
end
