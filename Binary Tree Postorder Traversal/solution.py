# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answers = []
        self.helper(root, answers)
        return answers
        
    def helper(self, node, answers):
        if node == None:
            return
        self.helper(node.left, answers)
        self.helper(node.right, answers)
        answers.append(node.val)
