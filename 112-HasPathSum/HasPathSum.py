# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(_self, _root, _targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if (_root == None):
            return False
        return _self.helperFunction(_root, _targetSum, 0)

    def helperFunction(_self, _root, _targetSum, _sum):
        if (_root.left == None and _root.right == None):
            return _targetSum == _sum + _root.val
        result1 = False
        result2 = False
        if _root.left != None:
            result1 = _self.helperFunction(_root.left, _targetSum, _sum + _root.val)
        if _root.right != None:
            result2 = _self.helperFunction(_root.right, _targetSum, _sum + _root.val)
        return result1 or result2
