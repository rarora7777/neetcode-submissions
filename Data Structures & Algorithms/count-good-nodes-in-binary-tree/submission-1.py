# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        num_good = 1
        
        stack = []
        stack.append((root, root.val))

        while stack:
            node, max_val = stack.pop()
            for child in [node.left, node.right]:
                if child:
                    stack.append((child, max(max_val, child.val)))
                    if child.val >= max_val:
                        num_good += 1
        
        return num_good

