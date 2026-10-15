# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        def find_depth(root):
            if root is None:
                return 0

            else:
                leftHeight = find_depth(root.left)
                rightHeight = find_depth(root.right)

                return 1 + max(leftHeight, rightHeight)

        return find_depth(root)
