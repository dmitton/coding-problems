# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answers = []
        self.helper(root, answers)
        return answers
        
    def helper(self, node, answers):
        if node == None:
            return
        answers.append(node.val)
        self.helper(node.left, answers)
        self.helper(node.right, answers)
