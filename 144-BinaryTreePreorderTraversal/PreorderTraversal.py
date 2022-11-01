# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None: return None
        curNode = root
        visitedNodes = []
        traversals = []
        while True:
            if curNode.left == None and curNode.right == None:
                traversals.append(curNode.val)
                if visitedNodes == []: break
                else:
                    curNode = visitedNodes.pop(-1)
                    while visitedNodes != [] and curNode.right == None:
                        curNode = visitedNodes.pop(-1)
                    if curNode.right != None:
                        curNode = curNode.right
                        continue
                    else: break
            while curNode.left != None:
                traversals.append(curNode.val)
                visitedNodes.append(curNode)
                curNode = curNode.left
            if curNode.right != None:
                if curNode.left == None:
                    traversals.append(curNode.val)
                curNode = curNode.right
        return traversals
