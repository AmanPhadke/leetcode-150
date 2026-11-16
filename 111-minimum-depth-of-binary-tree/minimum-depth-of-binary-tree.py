# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def minDepth(self, root):
        if not root:
            return 0

        queue = deque([root])
        level_count = 0

        while queue:
            level_count += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.right:
                    queue.append(node.right)

                if node.left:
                    queue.append(node.left)

                

                if not node.left and not node.right:
                    return level_count
                    




        
        