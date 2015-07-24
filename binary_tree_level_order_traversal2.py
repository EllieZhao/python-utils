class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def __init__(self):
        self.s = []
    # @param {TreeNode} root
    # @return {integer[][]}
    def levelOrderBottom(self, root):
        if not root:
            return []
        self.DFS(root, 0)
        return self.s[::-1]

    def DFS(self, root, level):
        if not root:
            return root
        if level == len(self.s):
            self.s.append([])
        self.s[level].append(root.val)
        self.DFS(root.left, level+1)
        self.DFS(root.right, level+1)

    def breadthFirstSearch(self, root):
        q = []
        if not root or (not root.left and not root.right):
            return root
        q.append(root)
        while q:
            t = q.pop(0)
            print t.val
            if t.left:
                print "t.left", t.left.val
                q.append(t.left)
            if t.right:
                print "t.right", t.right.val
                q.append(t.right)

    def depthFirstSearch(self, root):
        q = []
        if not root or (not root.left and not root.right):
            return root
        q.append(root)
        while q:
            t = q.pop()
            print t.val
            if t.right:
                print "t.right", t.right.val
                q.append(t.right)
            if t.left:
                print "t.left", t.left.val
                q.append(t.left)

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
#s.breadthFirstSearch(n1)
#s.depthFirstSearch(n1)
print s.levelOrderBottom(n1)
