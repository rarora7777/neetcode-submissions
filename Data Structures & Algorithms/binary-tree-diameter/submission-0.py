# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:        
        if not root:
            return 0

        return self.heightAndDiam(root)[1]

    def heightAndDiam(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0, 0

        leftHeight, leftDiam = self.heightAndDiam(root.left)
        rightHeight, rightDiam = self.heightAndDiam(root.right)

        height = 1 + max(leftHeight, rightHeight)
        selfDiam = leftHeight + rightHeight

        return height, max(max(selfDiam, leftDiam), rightDiam)





