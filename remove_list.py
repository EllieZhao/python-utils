# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        while head:
            if head.val == val:
                head = head.next
            else:
                break
        if not head:
            return None
        
        p = head
        q = head.next
        while q:
            while q and q.val == val:
                p.next = q.next
                q = q.next
            p = p.next
            if p:
                q = p.next
            else:
                q = None
        return head
                
            


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(2)
l8 = ListNode(2)
l9 = ListNode(2)


l1.next = l2
l2.next = l8
l4.next = l9
l6.next = l8
l8.next = l9

l3 = None
#l3.next = l5
l5.next = l7
l7.next = None

x = Solution()
l = x.removeElements(l1,2)
while l:
    print l.val
    l = l.next
