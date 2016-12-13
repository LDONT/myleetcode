/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class BSTIterator {      //二叉搜索树找最小。时间复杂度o(1),空间o(h)
    private Stack <TreeNode> stack = new Stack <TreeNode> ();

    public BSTIterator(TreeNode root) {
        pushleft(root);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode t = stack.pop();
        pushleft(t.right);
        return t.val;
    }
    
    public void pushleft(TreeNode root){      //把左边节点压入栈
        for(; root != null; root = root.left){
            stack.push(root);
        }
    }
}

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = new BSTIterator(root);
 * while (i.hasNext()) v[f()] = i.next();
 */