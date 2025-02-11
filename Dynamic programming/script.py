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

#arr=[1,-12,-4,5,8]
#get_max_sum_subarray(arr)



#----------------------------------------- prime XOR -------------------------------------------

from itertools import combinations


def handle_error_excpetion_and_logs(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print(f"calling function {func.__name__} with arguments {args} ")
            results= func(*args,**kwargs)
            print(f"function {func.__name__} returned results: {results}")
            return results
        except Exception as e:
            print(f"An ERROR occured during executing {func.__name__}: {e}")
            return None
    return wrapper


@handle_error_excpetion_and_logs
def get_prime_XOR(arr : list[int]):
    prime_combis=[]
    for i in range (1,len(arr)+1):
        combis=[rec for rec in list(combinations(arr,i))]
        for combi in combis:
            prime_combi=get_XOR(list(combi))
            if (get_is_prime(prime_combi)):
                prime_combis.append(prime_combi)
    return prime_combis

@handle_error_excpetion_and_logs
def get_XOR(arr :list[int]):
    result=0
    for i in arr:
        result ^=i
    return result


@handle_error_excpetion_and_logs
def get_is_prime(a :int):
    is_prime=False
    for i in range(2,a):
        if a%i ==0:
            return is_prime
    is_prime=True
    return is_prime



arr=[3511,3671,4153  ]
print(get_prime_XOR(arr))