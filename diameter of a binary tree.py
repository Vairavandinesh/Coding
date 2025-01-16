# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.largest_depth=0
        def dfs(root):
            if root == None:
                return 0
            leftheight=dfs(root.left)
            rightheight=dfs(root.right)
            self.largest_depth=max(self.largest_depth,leftheight+rightheight)
            return 1+max(leftheight,rightheight)
        dfs(root)
        return self.largest_depth