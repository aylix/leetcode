from collections import Counter
import numpy as np

def find_sparse_array_num(s,queries):
    nums=[np.count_nonzero(np.array(s)==rec) for rec in queries]
    return nums

import numpy as np
from collections import Counter
def valid_or_not(s):
    c=Counter(st)
    lst=[ c[i] for i in np.unique([d for d in st])]
    if len(np.where(np.array(lst)>1)[0])>1 or len(np.where(np.array(lst)>2)[0])>0:
        return "NO"
    else:
        return "YES"
    
def special_string(s):
    num=0
    for k in range (1,len(s)+1):
        for d in slide_string(s,k):
            if is_mirroring(d):
                 num+=1

    return num

def slide_string(s,k):
    slides=[]
    for i in range(0,len(s)-k+1):
        slides.append(s[i:i+k])
    return slides

def is_mirroring(s):
    if len(s)==1:
        return True
    mid=len(s)//2
    if s[:mid]==s[mid+1:] and s[0]!=s[mid] and s[len(s)-1]!=s[mid]:
        return True
    return False 


st="aba"
print(special_string(st))

s=["ad","dfgsg","df","rtz","dfgsg"]
queries=["df","dfgsg","v"]
print(find_sparse_array_num(s,queries))