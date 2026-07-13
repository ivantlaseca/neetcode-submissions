# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""

            1
        2       3

        1
        [2,3]
        
        Pop all elements from queue
        [3,2]

        Construct new tree using queue
        [3,2]
        root.left = queue.popLeft()
        root.right = queue.popLeft()

            1
        3       2


"""

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
            
        