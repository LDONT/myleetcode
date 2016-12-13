/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
 //plan1,利用二叉搜索树性质，类似二分法
public class Solution {      //找二叉搜索树中第k大
    public int kthSmallest(TreeNode root, int k) {
        int num = count(root.left);
        if (num+1 < k){     
            return kthSmallest(root.right, k-num-1);
        }
        if (num+1 > k){
            return kthSmallest(root.left,k);
        }
        return root.val;
    }
    private int count(TreeNode root){
        if (root == null){
            return 0;
        }
        return 1 + count(root.right) + count(root.left);
    }
}

//plan2    递归深度优先搜索
public class Solution {
    private int count;
    private int ret;
    public int kthSmallest(TreeNode root, int k) {
        count = k;
        deepfind(root);
        return ret;
    }
    private void deepfind(TreeNode root){
        if(root.left != null){
            deepfind(root.left);
        }
        count--;
        if(count == 0){
            ret = root.val;
            return;
        }
        if(root.right != null){
            deepfind(root.right);
        }
    }
}