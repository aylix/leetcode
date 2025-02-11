

class Tree:

    def __init__(self,data):
        self.data=data
        self.right=None
        self.left=None

    
    def if_binary_search_tree(self,current_node):
        if current_node.left is None and current_node.right is None:
            return True
        right_sub=True
        if current_node.right is not None:
            right_sub=current_node.data<current_node.right.data and self.if_binary_search_tree(current_node.right)
        left_sub=True
        if current_node.left is not None:
            left_sub=current_node.data>current_node.left.data and self.if_binary_search_tree(current_node.left)
        return right_sub and left_sub

root=Tree(0)
root.right=Tree(3)
root.left=Tree(2)
root.left.left=Tree(1)

print(root.if_binary_search_tree(root))

