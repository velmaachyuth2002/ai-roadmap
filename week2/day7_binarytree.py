from collections import deque


class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def max_depth(root):
    if root is None:
        return 0
    left_depth=max_depth(root.left)
    right_depth=max_depth(root.right)
    return 1+max(left_depth,right_depth)

def inorder(root):
   
    if root is None:
        return []
   
    return inorder(root.left) + [root.val] + inorder(root.right)
    

def bfs(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return result
 
list1=[]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(max_depth(root))   
print(inorder(root))    
print(bfs(root))        


print(max_depth(None))
print(inorder(None))     
print(bfs(None))     