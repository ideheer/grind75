"""
Code generated by https://github.com/goodstudyqaq/leetcode-local-tester
"""
from collections import deque

try:
    from utils.python3.help import *
except ImportError:
    pass # In leetcode environment, we don't need to import the help file.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        result = []
        q.append(root)
        while q:
            qLen = len(q)
            row = []
            for item in range(qLen):
                curr = q.popleft()
                if curr:
                    row.append(curr.val)
                    if curr.left:
                        q.append(curr.left)
                    if curr.right:
                        q.append(curr.right)
            result.append(row)
        return result
                    