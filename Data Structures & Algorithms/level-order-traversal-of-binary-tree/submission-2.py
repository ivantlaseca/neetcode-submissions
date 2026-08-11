# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
Algo:

1. Queue, add first node
2. While the queue is not empty, take the current size of the queue (level)
a. Add elements on the current level to a list
b. Add the children of these elements to the queue
c. Add that list to an output list
3. Return output

O(n)

Input: root = [1,2,3,4,5,6,7]
Output: [[1],[2,3],[4,5,6,7]]

Input: root = [1]
Output: [[1]]

Input: root = []
Output: []
"""
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        out = []
        while q:
            size = len(q)
            level = []
            for i in range(size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                level.append(node.val)
            out.append(level)
        return out
            

