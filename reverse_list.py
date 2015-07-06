# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def reverseList(self, head):
        if not head or not head.next:
            return head

        p = head
        head = None
        while p:
            tmp = p.next
            p.next = head
            head = p
            p = tmp
        return head

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
l2.next = l4
l4.next = l6
l6.next = l8

l3 = None
#l3.next = l5
l5.next = l7
l7.next = None

x = Solution()
l = x.reverseList(l1)
while l:
    print l.val
    l = l.next
