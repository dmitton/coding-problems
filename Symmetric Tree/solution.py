# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        else:
            return self.helper(root.left, root.right)
    
    def helper(self, leftTreeNode, rightTreeNode):
        if leftTreeNode == None and rightTreeNode == None:
            return True
        elif leftTreeNode and rightTreeNode and (leftTreeNode.val == rightTreeNode.val):
            return self.helper(leftTreeNode.left, rightTreeNode.right) and      self.helper(leftTreeNode.right, rightTreeNode.left)
        else:
            return False
