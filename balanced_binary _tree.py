class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #create a helper function to return the height and to find if its balanced or not , without the helper , we have to write two functions to check . one for the height and one for the balance
        def helper(root):
            if not root:#means if the root is not present,the tree is balanced
                return True
            #calculate the left and right height recursively
            leftheight=helper(root.left)
            rightheight=helper(root.right)
            #check if any node reaches -1 or if the sum of left and rightbecomes >1 , is so ,its not a balanced tree
            if (leftheight==-1 or rightheight==-1 or abs(leftheight-rightheight)>1):
                return -1#the -1 has a purpose later , lets see
            return max(leftheight,rightheight)+1
        return helper(root)!=-1