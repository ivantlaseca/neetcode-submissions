# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
            3
        2       8

Base: If none, return 0

1 + max(maxD(left), maxD(right))
T, S: O(n)

            3
        2       8
o: 2
            3
o: 1

            []
o: 0

            3
        2       8
    2
1
o: 4

"""
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        