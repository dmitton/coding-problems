# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        return self.helper(root, float("-inf"), float("inf"))
        
    def helper(self, node, left, right):
        if node == None:
            return True
        if not (node.val < right and node.val > left):
            return False
        else:
            return self.helper(node.left, left, node.val) and self.helper(node.right, node.val, right)
