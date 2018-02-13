class TreeNode(object):

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def inorder_traverse(self, root):
        """
        O(n) time complexity: need to visit every node
        O(depth) / O(logn) of balanced tree: using DFS
        Use a stack LNR order.
        """
        result, stack = [], []

        while True:
            while root:
                # LEFT
                stack.append(root)
                root = root.left
            if not stack:
                return result
            
            # NODE
            node = stack.pop()
            result.append(node.val)

            # RIGHT
            root = node.right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        O(n) time complexity
        O(lgn) space
        """
        if len(nums) < 1:
            return
        
        mid = len(nums) // 2
        root = TreeNode(nums[mid])

        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        
        return root

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left_depth = 1 + self.maxDepth(root.left)
        right_depth = 1 + self.maxDepth(root.right)
        return max(left_depth, right_depth)


class Solution:
    # @param {TreeNode} root
    # @return {integer}
    def maxDepth(self, root):
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))