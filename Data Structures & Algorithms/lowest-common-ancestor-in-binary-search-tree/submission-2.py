# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root
        while cur:
            # Both p and q are in the left subtree
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            # Both p and q are in the right subtree
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            # Either p or q (or both) are cur, so cur is the LCA.
            # Or p and q are in two different subtrees, so cur is the LCA.
            else:
                return cur
        
        return cur

        