class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# root = Node(5)
# root.left = Node(3)
# root.right = Node(1)

# Traversal
class PreOrder:
    def solve(self, root, L):
        if(root == None):
            return
        L.append(root.val)
        self.solve(root.left, L)
        self.solve(root.right, L)

    def preorderTraversal(self, root: Node | None) -> list[int]:
        L = []
        self.solve(root, L)
        return L
class InOrder:
    def solve(self, root, ans):
        if not root:
            return
        self.solve(root.left, ans)
        self.solve(root.right, ans)
        ans.append(root.val)
        
    def postorderTraversal(self, root: Node | None) -> list[int]:
        ans = []
        self.solve(root, ans)
        return ans
    
class PostOrder:
    def solve(self, root, ans):
        if not root:
            return
        self.solve(root.left, ans)
        self.solve(root.right, ans)
        ans.append(root.val)
        
    def postorderTraversal(self, root: Node | None) -> list[int]:
        ans = []
        self.solve(root, ans)
        return ans

from collections import deque       
class LevelOrder:
    def levelOrder(self, root: Node | None) -> list[list[int]]:
        if not root:
            return []
        
        ans = []
        queue = deque([root])
        while queue:
            size = len(queue)
            level = []

            for _ in range(size):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            ans.append(level)
        return ans