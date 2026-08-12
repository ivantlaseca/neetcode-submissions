# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Algo:

1. DFS
a. Base: If None, return True
b. if not left < root.val < right, return False
c. Process left and right subtrees

2. DFS on root with appropriate boundaries

T: O(n)
S: O(n)
"""
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, left, right):
            if not root:
                return True
            if not left < root.val < right:
                return False
            return validate(root.left, left, root.val) and validate(root.right, root.val, right)
        return validate (root, float("-inf"), float("inf"))

        