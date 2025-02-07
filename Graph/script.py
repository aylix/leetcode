#https://www.hackerrank.com/challenges/journey-to-the-moon/problem?isFullScreen=true

import numpy as np
import functools


def log_exception_handle(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f" Calling function {func.__name__} with args : {args}")
            result=func(*args,**kwargs)
            print(f"Function {func.__name__} return results: {result}")
            return result
        except Exception as e:
            print(f"Error occured during executing {func.__name__} ERROR: {e}")
            return None
    return wrapper


@log_exception_handle
def find_pair_numbers(arr :list[list[int]]):
    group=[]
    for i in range(0,len(arr)):

        linked_pairs=[(elem,arr[i]) for elem in arr if len(np.intersect1d(elem,arr[i]))>0 and elem!=arr[i]]
        same_group=set(np.array(linked_pairs).flatten())
        group.append({int(g) for g in same_group})
        group=list(set(map(frozenset,group)))
    lens=[len(rec) for rec in group]
    return np.sum(lens)




arr=[[5,3],
     [2,3],
     [0,4]]


find_pair_numbers(arr)