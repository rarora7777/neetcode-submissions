# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    balanced: bool = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        self.balanced = True

        _ = self.height(root)

        return self.balanced
    
    def height(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)

        if abs(leftHeight - rightHeight) > 1:
            self.balanced = False
        
        return 1 + max(leftHeight, rightHeight)
    