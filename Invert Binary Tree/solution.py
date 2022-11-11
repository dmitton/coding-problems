# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return root
        if root.left == None and root.right == None:
            return root
        else:
            self.helper(root, root.left, root.right)
            return root
        
    def helper(self, node, leftNode, rightNode):
        if leftNode == None and rightNode == None:
            return
        else:
            temp = leftNode
            leftNode = rightNode
            rightNode = temp
            node.left = leftNode
            node.right = rightNode
            if node.left != None:
                self.helper(node.left, leftNode.left, leftNode.right)
            if node.right != None:
                self.helper(node.right, rightNode.left, rightNode.right)
