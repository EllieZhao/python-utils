class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome2(self, head):
        old = []
        new = []
        p = head
        while p:
            old.append(p.val)
            new.insert(0, p.val)
            p = p.next
        return old == new

    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        slow = slow.next
        p = slow.next
        slow.next = None
        while p:
            q = p.next
            p.next = slow
            slow = p
            p = q
        while slow:
            if slow.val == head.val:
                head = head.next
                slow = slow.next
            else:
                return False
        return True

s = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(3)
n5 = ListNode(0)
n6 = ListNode(1)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6


print s.isPalindrome(n1)
