# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = self.helper(root)
        return answer
    
    def helper(self, node):
        if node == None:
            return 0
        else:
            lheight = self.helper(node.left)
            rheight = self.helper(node.right)
            
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
