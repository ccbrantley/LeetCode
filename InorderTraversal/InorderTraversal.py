# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        return self.helperFunction(root, [])

    def helperFunction(self, root, traversal = []):
        if root.left != None:
            traversal = self.helperFunction(root.left, traversal)
        traversal.append(root.val)
        if root.right != None:
            traversal = self.helperFunction(root.right, traversal)
        return traversal
