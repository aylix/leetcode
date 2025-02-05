from collections import Counter
import numpy as np

def find_sparse_array_num(s,queries):
    nums=[np.count_nonzero(np.array(s)==rec) for rec in queries]
    return nums


s=["ad","dfgsg","df","rtz","dfgsg"]
queries=["df","dfgsg","v"]
print(find_sparse_array_num(s,queries))