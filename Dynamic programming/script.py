#https://www.hackerrank.com/challenges/maxsubarray/problem?isFullScreen=true

import numpy as np
import functools

def log_and_handle_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f"Calling {func.__name__}")
            result=func(*args,**kwargs)
            print(f"{func.__name__} returned: {result}")
            return result
        except Exception as e:
            print(f" Error in {func.__name__} : {e}")
            return None
    return wrapper


@log_and_handle_exceptions
def get_max_sum_subarray(arr :list[int]):
    if (len(arr)==0):
        return -1
    arr.sort()
    if arr[0]<0:
        if arr[len(arr)-1]>0:
            #jump to biggest negative num Index
            index=get_biggest_negative_index_sorted(arr)
            return len(arr[index+1:])
        else:
            return 1
    else:
        return len(arr)-1

@log_and_handle_exceptions
def get_biggest_negative_index_sorted(arr):
    arr.sort()
    return np.argmax(np.array(arr)[np.where(np.array(arr)<0)[0]])


arr=[1,-12,-4,5,8]
get_max_sum_subarray(arr)