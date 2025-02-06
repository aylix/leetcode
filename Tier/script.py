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
        

    def count_words_under_node(self,node :Tiernode,count):
        
        if len(node.children)==0:
            return count
        c=count+np.count_nonzero(np.array([node.children[child].is_end_of_word for child in node.children]))
        for ch in node.children:
            #count=count+np.count_nonzero(np.array([node.children[child].is_end_of_word for child in node.children]))
            c=c+self.count_words_under_node(node.children[ch],count)
            
        return c
    




    def statrs_with(self,partial):
        current_node=self.root
        count=0
        for i in range(0,len(partial)):
            children=current_node.get_children_names() 
            if  partial[i] in children : 
                count=count+np.count_nonzero(np.array([current_node.children[ch].is_end_of_word for ch in children]))
                # move current node to the child  repesenting next char
                current_node=current_node.children[partial[i]]
            # retun 0 where not all of the partial exists
            else:
                return 0
            


        return self.count_words_under_node(current_node,count)





root=Tiernode()
tier=Tier(root)
tier.insert("car")
tier.insert("cara")
tier.insert("cat")
tier.insert("aylar")
#tier.print(root)
print(tier.statrs_with("car"))
#print(tier.count_leave(root))