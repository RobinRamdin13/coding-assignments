from sys import stdin
from typing import List

def main(capacity:int, weights:List, values:List)->float:
    """Function to compute the maximum value of items
    that fit into the backpack defined by capacity

    Args:
        capacity (int): backpack weight limit
        weights (List): individual items weights
        value (List): individual items values

    Returns:
        float: maximum value
    """        
    output = 0
    value_per_weigth = [a/b for a,b in zip(values,weights)]
    max_value_sort = value_per_weigth.copy() # create a copy 
    max_value_sort.sort(reverse=True) # sort by descending order
    while capacity != 0:
        max_index = value_per_weigth.index(max_value_sort[0]) # find the max index
        # max index weight is less than capacity
        if weights[max_index] <= capacity:
            output += values[max_index]
            capacity -= weights[max_index]
        else: 
            output += capacity*value_per_weigth[max_index]
            capacity = 0
        max_value_sort = max_value_sort[1:]
        if len(max_value_sort) == 0: break
    return output

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = main(capacity, weights, values)
    print("{:.10f}".format(opt_value))