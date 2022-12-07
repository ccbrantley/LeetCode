# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        queue = [root]
        while queue != []:
            curNode = queue.pop(0)
            if curNode.left == None and curNode.right == None:
                continue
            elif curNode.left == None:
                curNode.left = curNode.right
                curNode.right = None
                queue.append(curNode.left)
            elif curNode.right == None:
                curNode.right = curNode.left
                curNode.left = None
                queue.append(curNode.right)
            else:
                tempNode = curNode.right
                curNode.right = curNode.left
                curNode.left = tempNode
                queue.append(curNode.left)
                queue.append(curNode.right)
        return root
