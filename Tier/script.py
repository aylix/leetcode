import numpy as np

class Tiernode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word= False
    def get_children_names(self):
        return [c for c in self.children]



class Tier:
    def __init__(self,root :Tiernode):
        self.root=root

    def insert(self,name :str):
        current_node=self.root
        for i in range(0,len(name)):
            node_names=current_node.get_children_names()
            if name[i] in node_names:
                childnode=current_node.children[name[i]]
            else:
                childnode=Tiernode()
                current_node.children[name[i]]=childnode
            if i==len(name)-1 :
                childnode.is_end_of_word=True 
              
            current_node=childnode
        



    def count_words_under_node(self,node :Tiernode,lst):
        
        if(node.is_end_of_word and  node not in lst):
            lst.append(node)
        for child in node.children:
            if node.children[child].is_end_of_word and node.children[child] not in lst:
                lst.append(node.children[child])
            self.count_words_under_node(node.children[child],lst)
 
        return len(lst)
        


    def statrs_with(self,partial):
        current_node=self.root
        for i in range(0,len(partial)):
            children_names=current_node.get_children_names()
            #print(children_names)
            if partial[i] in children_names:
                current_node=current_node.children[partial[i]]
            else:
                return 0
        return self.count_words_under_node(current_node,[])
            
            
            





root=Tiernode()
tier=Tier(root)
tier.insert("hack")
tier.insert("hackerrank")

#tier.print(root)
print(tier.statrs_with("hak"))
#print(tier.count_leave(root))