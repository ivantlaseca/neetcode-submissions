# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
	5
3		8
True


"""


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validateTree(root, leftBoundary, rightBoundary):
            if not root:
                return True
            if not leftBoundary < root.val < rightBoundary:
                return False
            return validateTree(root.left, leftBoundary, root.val) and validateTree(root.right, root.val, rightBoundary)
        return validateTree(root, float("-inf"), float("inf"))
        
        