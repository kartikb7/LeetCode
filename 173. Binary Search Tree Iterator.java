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
class BSTIterator {

    Stack<TreeNode> stack = new Stack<TreeNode>();
    public BSTIterator(TreeNode root) {
        TreeNode start = root;
        if (start != null) {
            stack.push(start);
            while (start.left != null) {
                start = start.left;
                stack.push(start);
            }
        }
    }
    
    /** @return the next smallest number */
    public int next() {
        TreeNode nextNode = stack.pop();
        int nextNodeData = nextNode.val;
        if (nextNode.right != null) {
            nextNode = nextNode.right;
            stack.push(nextNode);
            while (nextNode.left != null) {
                nextNode = nextNode.left;
                stack.push(nextNode);
            }
        }
        return nextNodeData;
    }
    
    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }
}

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator obj = new BSTIterator(root);
 * int param_1 = obj.next();
 * boolean param_2 = obj.hasNext();
 */