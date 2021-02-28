/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */
var inorderTraversal = function(root) {
    
    const res = [];
    
    function helper(node, res) {
        if (!node) return;
        helper(node.left, res)
        res.push(node.val)
        helper(node.right, res)
    }
    helper(root, res)
    return res
};
