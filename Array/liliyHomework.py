import numpy as np

def get_min_swap_num(arr :list[int]):
    sorted_arr=sorted(arr)
    distances=[arr.index(rec)-sorted_arr.index(rec) for rec in arr]
    min_swap=0
    temp_index=0
    while arr!=sorted_arr and temp_index<len(arr)-1:
        print(np.argmax(distances),np.argmin(distances),arr)
        arr=swap([arr[np.argmax(distances)],arr[np.argmin(distances)]],arr)
        distances=[arr.index(rec)-sorted_arr.index(rec) for rec in arr]
        temp_index+=1
        print("\n")

    return temp_index


def swap(pair,arr):
    first_elem_index=arr.index(pair[0])
    second_elem_index=arr.index(pair[1])
    arr[first_elem_index],arr[second_elem_index]=arr[second_elem_index],arr[first_elem_index]
    return arr

array=[7,15,12,3]
print(get_min_swap_num(array))