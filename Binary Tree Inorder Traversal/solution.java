/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer>solutions = new ArrayList();
        solutions = treeTraversal(root,solutions);
        return solutions;
    }
    
    public List<Integer>treeTraversal(TreeNode node,List<Integer>solutions){
        if(node == null){
            return solutions;
        }
        
        solutions = treeTraversal(node.left,solutions);
        solutions.add(node.val);
        solutions = treeTraversal(node.right,solutions);
        return solutions;
    }
}
