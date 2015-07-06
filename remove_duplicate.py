class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if not head or not head.next:
            return head
        p = head.next
        prev = head
        while p:
            if prev.val == p.val:
                prev.next = p.next
            else:
                prev = p
            p = p.next
        return head
                
s = Solution()

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(2)
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3

new = s.deleteDuplicates(n1)
while new:
    print new.val
    new = new.next
