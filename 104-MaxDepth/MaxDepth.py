# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        return self.helperFunction(root, 1)

    def helperFunction(_self, _root, _maxDepth = 1):
        maxDepth = _maxDepth
        if _root.left != None:
            maxDepth = max(_maxDepth, _self.helperFunction(_root.left, _maxDepth + 1))
        if _root.right != None:
            maxDepth = max(maxDepth, _self.helperFunction(_root.right, _maxDepth + 1))
        return max(_maxDepth, maxDepth)
