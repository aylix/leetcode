
import numpy as np




class Tree():
    def __init__(self,name):
        self.name=name
        self.right=None
        self.left=None

    def add_right(self,node):
        self.right=node
    def add_left(self,node):
        self.left=node
    def get_right(self):
        return self.right
    def get_left(self):
        return self.left
    def get_name(self):
        return self.name

def inOrder_traversal(tree :Tree):

    if tree==None :
        return visits
    visits=visit_to_leaf(tree.get_left())
    visits.append(tree)
    
    return visits + visit_to_leaf(tree.get_right())

def visit_to_leaf(tree :Tree):
    parent=tree
    visits :list[Tree] =[]
    visits.append(tree)
    while (tree.get_left()!=None or tree.get_right()!=None):
        parent=tree
        if tree.get_left() != None:
            tree=tree.get_left()
            visits.append(tree)
        else:
            tree=tree.get_right()
    if (parent.get_right() !=None):
        visits.append(parent.get_right())
    return visits

def swap(tree :Tree,depth :int,k):
    if tree.get_left() ==None and tree.get_right()==None:
        return tree
    if depth%k==0:
        tree.add_left(swap(swap_subs(tree.get_left()),depth+1,k))
        tree.add_right(swap(swap_subs(tree.get_right()),depth+1,k))
    return tree



def swap_subs(tree :Tree):

    tree.left, tree.right =tree.right, tree.left
    return tree
        


def view_tree(tree :Tree,arr,lable,d):
    if tree==None:
        return arr
    arr.append({lable:tree.get_name(),"depth":d})
    view_tree(tree.get_left(),arr,"left",d+1)
    view_tree(tree.get_right(),arr,"right",d+1)
    return arr


def decodeHuff(root, s,r):
    if s=='':
        return r
    temp_root=root    
    i=0
    while temp_root.left!=None or temp_root.right!=None:
        if(s[i]=='0'):
            temp_root=temp_root.left
        else:
            temp_root=temp_root.right
        i+=1
    r=r+temp_root.name
    return decodeHuff(root,s[i:],r)


tree= Tree(0)
tree.add_left(Tree(1))
tree.add_right(Tree("A"))
tree.get_left().add_left(Tree('B'))
tree.get_left().add_right(Tree('C'))


print(decodeHuff(tree,"1001011",""))

#[print(node) for node in view_tree(tree,[],"ROOT",0)]
#tree=swap(tree,0,2)
#[print(node) for node in view_tree(tree,[],"ROOT",0)]


