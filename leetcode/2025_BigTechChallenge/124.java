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
    int ans;
    public int maxPathSum(TreeNode root) {
        ans = -1000;
        bfs(root);
        return ans;
    }

    int bfs(TreeNode node) {
        if (node == null) return 0;
        int sumL = Math.max(bfs(node.left), 0);
        int sumR = Math.max(bfs(node.right), 0);
        ans = Math.max(ans, sumL + sumR + node.val);
        return Math.max(sumL, sumR) + node.val;
    }
}