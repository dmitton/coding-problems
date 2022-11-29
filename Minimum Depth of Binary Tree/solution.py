# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        depth = self.helper(root, 1, 1)
        return depth
    
    def helper(self, node, depth, minimum):
        if node.left == None and not node.right == None:
            minimum = self.helper(node.right, depth + 1, minimum)
            return minimum
        elif not node.left == None and node.right == None:
            minimum = self.helper(node.left, depth + 1, minimum)
            return minimum
        elif node.left == None and node.right == None:
            if minimum == 1:
                minimum = depth
            elif depth < minimum:
                minimum = depth
            return minimum
        else:
            minimum = self.helper(node.left, depth + 1, minimum)
            minimum = self.helper(node.right, depth + 1, minimum)
            return minimum
