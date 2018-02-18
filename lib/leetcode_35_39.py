##36 valid Sudoku


board = [[".","8","7","6","5","4","3","2","1"],["2",".",".",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]
board = [["00","01","02","6","5","4","3","2","1"],["10","11.","21",".",".",".",".",".","."],["3",".",".",".",".",".",".",".","."],["4",".",".",".",".",".",".",".","."],["5",".",".",".",".",".",".",".","."],["6",".",".",".",".",".",".",".","."],["7",".",".",".",".",".",".",".","."],["8",".",".",".",".",".",".",".","."],["9",".",".",".",".",".",".",".","."]]


def isValidSudoku(board):
    for row in range(0,len(board)):
        count = set()
        for element in board[row]:
            if element == ".":
                continue
            if element in count:
                return False
            else:
                count.add(element)
    for column in range(0, len(board)):
        count = set()
        for row in range(len(board)):
            element = board[row][column]
            if element == ".":
                continue
            if element in count:
                return False
            else:
                count.add(element)
    for col in range(0,3):
        for grid in range(0,3):
            print "reset grid "
            print grid
            count = set()
            for i in range(0  + (grid * 3),3 + (3 *grid)):
                for j in range(0 + (col * 3),3 + (3*col)):
                    print "i, j"
                    print i, j
                    element = board[i][j]
                    print element
                    if element == ".":
                        continue
                    if element in count:
                        return False
                    else:
                        count.add(element)
                print count
    return True




##39 Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
#candiates [2, 3, 6, 7], target = 7,


a = [2, 3, 6, 7]
target = 7
def combinationSum(candidates, target):
    result = []
    candidates = sorted(candidates)
    print candidates
    def dfs(remain, stack):
        print "remain"
        print remain
        print "stack"
        print stack
        if remain == 0:
            result.append(stack)
            print "result"
            print result
            return
        for item in candidates:
            if item > remain:
                print "breakt"
                print "item"
                print item
                print remain
                break
            if stack and item < stack[-1]:
                print "continue"
                print "stack"
                print stack
                print "item"
                print item
                continue
            else:
                print "dfs"
                print "stack"
                print stack
                print "item"
                print item
                dfs(remain - item, stack + [item])
    dfs(target, [])
    return result

combinationSum(a, target)


#round 2
def combinationSum(candidates, target):
    result = []
    combinationSumRecu(sorted(candidates), result, 0, [], target)
    return result

def combinationSumRecu(candidates, result, start, intermediate, target):
    if target == 0:
        result.append(list(intermediate))
    while start < len(candidates) and candidates[start] <= target:
        intermediate.append(candidates[start])
        combinationSumRecu(candidates, result, start, intermediate, target - candidates[start])
        intermediate.pop()
        start += 1
