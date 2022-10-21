# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.helperFunction(root, root, True)

    def helperFunction(_self, _r1, _r2, _truth):
        if _r1.left != None:
            if _r2.right != None:
                _truth = _truth and _self.helperFunction(_r1.left, _r2.right, _truth)
            else:
                return False
        if _r1.val != _r2.val:
            return False
        if _r1.right != None:
            if _r2.left != None:
                _truth = _truth and _self.helperFunction(_r1.right, _r2.left, _truth)
            else:
                return False
        return _truth
