# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        q = deque()

        max_level = -1
        q.append((root, 0))

        while q:
            node, level = q.popleft()
            if level > max_level:
                res.append(node.val)
                max_level = level
            if node.right:
                q.append((node.right, level+1))
            if node.left:
                q.append((node.left, level+1))
        
        return res

