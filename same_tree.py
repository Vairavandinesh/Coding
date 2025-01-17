class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #if both roots of p and q are null , we can say its same
        if not p and not q:
            return True
        # if one root has child and other dont,its an imbalance .moreover , eventhough the nodes are same but if the values differ , it is also an error ,using or operator to check if one of the 3 conditions in false, its an error
        elif not p or not q or p.val!=q.val:
            return False
        #final condition: return True if the left of p and left of q are equal and the right of p and right of q are equal
        return (self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))