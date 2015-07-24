class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def invertTree(self, root):
        if not root or (not root.left and not root.right):
            return root
        t = root.left
        root.left = root.right
        root.right = t
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n7
n4.left = n6

s = Solution()
t = s.invertTree(n1)
print t.val
print t.left.val
print t.right.val
