# Operations on BST ... SEARCH
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:  # O(height)
    def searchBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        if root is None:
            return None
        
        curr = root

        while curr is not None:
            if curr.val == val:
                return curr
            elif curr.val < val:
                curr = curr.right
            else:
                curr = curr.left
        
        return None

# Operations on BST ... INSERT
class Solution:
    def insertIntoBST(self, root: TreeNode | None, val: int) -> TreeNode | None:
        newNode = TreeNode(val)

        if root is None:
            return newNode
        
        curr = root
        while curr is not None:
            if val < curr.val:
                # left
                if curr.left is not None:
                    curr = curr.left
                else:
                    curr.left = newNode
                    break
            else:
                # right
                if curr.right is not None:
                    curr = curr.right
                else:
                    curr.right = newNode
                    break
        
        return root 

# Operations on BST ... DELETE
class Solution:
    def deleteNode(self, root: TreeNode | None, key: int) -> TreeNode | None:
        # base case
        if root is None:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                # finding inorder successor and replacing the deleted node while deleting the original successor
                temp = root.right
                while temp.left is not None:
                    temp = temp.left
                root.val = temp.val
                root.right = self.deleteNode(root.right,temp.val)
        return root

# Operations on BST ... VALIDATE
class Solution:
    def isPossible(self, root, mn, mx):
        if root is None:
            return True
        if root.val < mn or root.val > mx:
            return False
        
        left = self.isPossible(root.left, mn, root.val-1)
        right = self.isPossible(root.right, root.val+1, mx)

        return left and right
    
    def isValidBST(self, root: TreeNode | None) -> bool:
        return self.isPossible(root, -100000000000000, 100000000000000)