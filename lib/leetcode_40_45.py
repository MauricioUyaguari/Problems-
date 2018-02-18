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
