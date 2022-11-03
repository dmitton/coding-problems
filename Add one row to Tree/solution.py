# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            newNode = TreeNode(val, root, None)
            return newNode
        else:
            self.helper(root, val, depth, 1)
            return root

    def helper(self, node, value, level, levelAt):
        if node == None:
            return
    
        if levelAt == (level - 1):
            #insert the value into the tree
            newNodeLeft = TreeNode(value, node.left, None)
            newNodeRight = TreeNode(value, None, node.right)
            node.left = newNodeLeft
            node.right = newNodeRight
            return

        # initial searching through the tree
        self.helper(node.left, value, level, levelAt + 1)
        self.helper(node.right, value, level, levelAt + 1)
        return
        
