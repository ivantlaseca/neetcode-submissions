# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
            5
        3       8
         9          10


(-inf, 3)

(9, 3, 5)

"""

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, lowerBoundary, upperBoundary):
            if not root:
                return True
            if not (lowerBoundary < root.val < upperBoundary):
                return False
            return valid(root.left, lowerBoundary, root.val) and valid(root.right, root.val, upperBoundary)
        
        return valid(root, float('-inf'), float('inf'))
        