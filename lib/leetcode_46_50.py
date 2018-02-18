
#49 Given an array of strings

a = ["eat", "tea", "tan", "ate", "nat", "bat"]
b = ["","",""]
def groupAnagrams(strs):
    if len(strs) < 1:
        return []
    result = []
    while strs:
        first = strs.pop(0)
        temp_result = []
        temp_result.append(first)
        temp_hash = hash_counter(first)
        i = 0
        while i < len(strs):
            print "strs"
            print strs
            temp = strs[i]
            current_count =  hash_counter(temp)
            print "temp_hash"
            print temp_hash
            print "word"
            print temp
            print "current_count"
            print current_count
            print temp
            print "i"
            print i
            if current_count == temp_hash:
                temp_result.append(temp)
                strs.pop(i)
                i -= 1
            print "strs before adding"
            print strs
            i += 1
        result.append(temp_result)
    return result




def hash_counter(word):
    counter = {}
    for let in word:
        if let in counter:
            counter[let] += 1
        else:
            counter[let] = 1
    return counter

groupAnagrams(b)


## 46


class Solution(object):
def groupAnagrams(strs):
    ans = collections.defaultdict(list)
    print ans
    for s in strs:
        print "s"
        print s
        count = [0] * 26
        for c in s:
            print "c"
            print c
            count[ord(c) - ord('a')] += 1
        print "tuple"
        print count
        print tuple(count)
        ans[tuple(count)].append(s)
        print ans
    return ans.values()


groupAnagrams(a)
