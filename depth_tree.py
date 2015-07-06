class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0
        left = self.maxDepth(root.left) + 1
        right = self.maxDepth(root.right) + 1
        return left if left > right else right

    def minDepth(self, root):
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        depth = min(left, right) if min(left, right) else max(left, right)
        return 1 + depth 
      
right3 = TreeNode(6)
right3.left = None
right3.right = None

right2 = TreeNode(5)
right2.left = None
right2.right2 = right3

left2 = TreeNode(4)
left2.left = None
left2.right = right2

left1 = TreeNode(2)
left1.left = left2
left1.right = right2

right1 = TreeNode(3)
right1.left = None
right1.right = None

root = TreeNode(1)
root.left = left1
root.right = right1

s = Solution()
#print s.maxDepth(root)
#
#        1
#    2       3
# 4    5
#        6

root = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n5 = TreeNode(5)
n6 = TreeNode(6)
n7 = TreeNode(7)
n8 = TreeNode(8)
root.left = n2
n2.right = n3
n3.left = n4
n4.right = n5
n5.left = n6
n6.right = n7
root.right = n8
#print s.maxDepth(root)
print s.minDepth(root)
