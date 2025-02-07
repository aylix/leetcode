import numpy as np
from collections import deque




def get_min_operation_num(arr :list[int],k :int):



    arr.sort()
    if len(arr)<2:
        return -1
    arr=deque(arr)
    op_num=0
    for i in range(0,len(arr)-1):

        combined_level=(arr[i])+(2)*arr[i]
        op_num+=1
        arr.popleft()
        arr.popleft()
        arr.append(combined_level)
        arr=list(arr)
        arr.sort()
        arr=deque(arr)
        if (arr[0]<k):
            continue
        else:
            return op_num
    return -1


queue=[]
queue.append(1)
queue.append(2)
queue.append(3)
queue.append(9)
queue.append(10)
queue.append(12)


print(get_min_operation_num(queue,7))