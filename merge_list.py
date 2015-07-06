# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        l = ListNode(None)
        idx = l
        while l1 and l2:
            x1 = l1.val
            x2 = l2.val
            if x1 < x2:
                idx.next = l1
                l1 = l1.next
            else:
                idx.next = l2
                l2 = l2.next
            idx = idx.next
        if l1:
            idx.next = l1
        if l2:
            idx.next = l2
        return l.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8)
l9 = ListNode(9)


l1.next = l2
#l2.next = l4
#l4.next = l6
#l6.next = l8

l3 = None
#l3.next = l5
#l5.next = l7
#l7.next = l9

x = Solution()
l = x.mergeTwoLists(l1, l3)
while l:
    print l.val
    l = l.next
