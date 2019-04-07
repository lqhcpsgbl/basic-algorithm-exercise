class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
          return 0
        # left is not None, but left has no children 
        if root.left is not None and root.left.left is None and root.left.right is None:
            left = root.left.val
        else:
            left = self.sumOfLeftLeaves(root.left)
        right = self.sumOfLeftLeaves(root.right)
        return left + right
