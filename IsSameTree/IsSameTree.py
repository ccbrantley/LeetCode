# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif p != None and q == None:
            return False
        pTraversal = self.helperFunction(p, [])
        qTraversal = self.helperFunction(q, [])
        for pNode, qNode in zip(pTraversal, qTraversal):
            if pNode != qNode:
                return False
        return True

    def helperFunction(_self, _root, _traversal = []):
        _traversal.append(_root.val)
        if (_root.left != None):
            _traversal = _self.helperFunction(_root.left, _traversal)
        else:
            _traversal.append(None)
        if (_root.right != None):
            _traversal = _self.helperFunction(_root.right, _traversal)
        else:
            _traversal.append(None)
        return _traversal
