class Solution {
    boolean isSumTree(Node root) {
        // Your code here
        if (root == null || (root.left == null && root.right == null)) {
            return true;
        }

        int leftSum = sum(root.left);
        int rightSum = sum(root.right);

        if ((root.data == leftSum + rightSum) && isSumTree(root.left) && isSumTree(root.right)) {
            return true;
        }
        
        return false;
    }
    private int sum(Node node) {
        if (node == null) {
            return 0;
        }
        return node.data + sum(node.left) + sum(node.right);
    }
}
