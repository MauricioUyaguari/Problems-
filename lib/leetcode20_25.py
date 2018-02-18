#22
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


def generateParenthesis(N):
    ans = []
    def backtrack(S = '', left = 0, right = 0):
        print "S"
        print S
        print "ans"
        print ans
        if len(S) == 2 * N:
            ans.append(S)
            print "first if, return"
            print ans
            return
        if left < N:
            print "left < N"
            backtrack(S + '(', left + 1, right)
        if right < left:
            print "right < left"
            backtrack(S + ')', left, right + 1)
    backtrack()
    return ans


## 24 Swap nodes in pairs
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)


def swapPairs(head):
    if head is None:
        return head
    dummy = ListNode(None)
    dummy.next = head
    current = dummy
    while current.next != None and current.next.next != None:
        lastNode = current.next.next.next
        switchx = current.next
        switchy = current.next.next
        current.next = switchy
        switchy.next = switchx
        switchx.next = lastNode
        print current.val
        print current.next.val
        print current.next.next.val
        print "change"
        current = current.next.next
        print current.val
    return dummy.next

check = swapPairs(head)
