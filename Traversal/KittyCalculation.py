
import numpy as np
from itertools import combinations
import math
class Graph():
    def __init__(self,adjc_matrix :list[list[int]]):
        self.matrix=adjc_matrix

    def calculate(self,query :list[int]):
        sum=0
        if (len(query)<2):
            return sum
        possible_pairs=[list(rec) for rec in combinations(query,2)]
        
        for pair in possible_pairs:
            path_len=self.find_shortest_path(list(pair))[0]
            sum=sum+(path_len*pair[0]*pair[1])
        result=sum%(math.pow(10,9)+7)

        return result
    
    def find_shortest_path(self,pair):

        src=pair[0]
        dst=pair[1]
        path=[]
        possible_dsts=np.where(np.array(self.matrix[src-1])==1)[0]
        possible_dsts=possible_dsts+1
        i=1
        while dst not in possible_dsts:
            srcs=possible_dsts
            dsts=np.array([ [int(rec)+1,s]  for s in srcs for rec in np.where(np.array(self.matrix[s-1])==1)[0]])
            path.append(dsts)
            possible_dsts=np.unique([d[0] for d in dsts])
            i+=1
        node=dst
        nodes=[]
        for j in range (len(path)-1,-1,-1):
            picked_node=[int(p[1]) for p in path[j] if int(p[0])==node][0]
            node=picked_node
            nodes.append(picked_node)
        return i,nodes[::-1]
        


graph=Graph([[0,1,1,1,0,0,0],
       [1,0,0,0,0,0,0],
       [1,0,0,0,1,1,1],
       [1,0,0,0,0,0,0],
       [0,0,1,0,0,0,0],
       [0,0,1,0,0,0,0],
       [0,0,1,0,0,0,0]    
       ])
query=[4,5,7]
print(graph.calculate([4,5,7]))
