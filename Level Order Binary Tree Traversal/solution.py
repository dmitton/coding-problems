# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answers = []
        height = self.height(root)
        for i in range(height):
            answers.append([])
        self.helper(root, answers, height)
        answers.reverse()
        return answers
    
    def helper(self, node, answers, height):
        if node == None:
            return
        answers[height - 1].append(node.val)
        self.helper(node.left, answers, height - 1)
        self.helper(node.right, answers, height - 1)
        return
    
    def height(self, node):
        if node == None:
            return 0
        else:
            lheight = self.height(node.left)
            rheight = self.height(node.right)
            
            if lheight > rheight:
                return lheight + 1
            else:
                return rheight + 1
