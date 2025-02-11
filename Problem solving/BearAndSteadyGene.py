
from itertools import combinations
from collections import Counter
import numpy as np

import functools

def handle_exceptions_and_logging(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        try:
            print(f"calling function {func.__name__} with args : {args}")
            result=func(*args,**kwargs)
            print(f" function {func.__name__} has been executed successfully and returned results : {result}")
            return result
        except Exception as e:    
            print(f" An ERROR occured during execution {func.__name__} : {e}")
            return None
    return wrapper
    

class SteadyGene:


    def __init__(self,gene :str,steady_letters):
        self.gene=gene
        self.letters=steady_letters
    
    @handle_exceptions_and_logging
    def get_all_subs_of_letters(self):
        subs=[]
        for i in range(1,len(self.letters)+1):
            [subs.append("".join(list(rec))) for rec in list(combinations(self.letters,i))]
        return subs
   
   
    @handle_exceptions_and_logging
    def find_smallest_substring(self):
        gene_subs=[]
        if not self.get_if_steady(self.gene):
            subs=np.array(self.get_all_subs_of_letters())
            for i in range(1,len(self.gene)+1):
                [gene_subs.append("".join(list(rec))) for rec in list(combinations(self.gene,i))]
            for gen_sub in gene_subs:
                subs_of_same_len=[s for s in subs if len(s)==len(gen_sub)]
                for sub in subs_of_same_len:
                    if (self.get_if_steady(self.gene.replace(gen_sub,sub))):
                        return gen_sub,len(gen_sub)
        return None

    @handle_exceptions_and_logging
    def get_if_steady(self,s):
        gene_counts=Counter(s)
        counts=[gene_counts[gene_count] for gene_count in gene_counts]
        return len(np.unique(np.array(counts)))==1
    
Gene=SteadyGene("AGCTAAAG","TCGA")
Gene.find_smallest_substring()