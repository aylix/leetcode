
import numpy as np
from itertools import combinations
from collections import Counter


def find_distribution(arr,k):
    plant_able_cities=np.count_nonzero(np.array(arr)==1)+1
    min=len(arr)+1
    for i in range(1,plant_able_cities):
        combinations_k_of_array=list(combinations(range(0,len(arr)),i))
        for elem in combinations_k_of_array:
            plant_cities=set(elem)
            not_plant_cities=set(range(0,len(arr)))-plant_cities
            all_possible_dists=np.array([b for a in plant_cities for b in not_plant_cities if np.abs(a-b)<k]).flatten()
            if not (Counter(list(not_plant_cities)) - Counter(all_possible_dists)) and all( arr[item]==1 for item in plant_cities):
                #print(min)
                min=np.min([min,len(plant_cities)])
                #print(plant_cities,not_plant_cities,all_possibles)
    if min>=len(arr):
        min=-1

    return min


arr=[0,1,1,1,0,0,0]
print(find_distribution(arr,3))