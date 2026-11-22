# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_list = []
        
        if not root:
            return level_list

        queue = deque()
        queue.append((root, 0))
        while queue:
            node, level = queue.popleft()
            if len(level_list) < level + 1:
                level_list.append([])
            level_list[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        
        return level_list