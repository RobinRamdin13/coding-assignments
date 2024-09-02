from typing import List

def binary_search(keys:List, query:int)->int:
    """Main function to run the helper function

    Args:
        keys (List): Array of keys
        query (int): Element of interest

    Returns:
        int: output from helper function
    """    
    return helper(keys, 0, len(keys)-1, query)

def helper(keys:List, low:int, high:int, query:int)->int:
    """Helper function to perform binary search recursively

    Args:
        keys (List): Array of keys
        low (int): lower bound
        high (int): upper bound
        query (int): element of interest

    Returns:
        int: position of element in array of keys, -1 if not present
    """     
    # if condition is not met the query does not exist
    if low <= high: 
        # instantiate the middle point
        middle_point = (low+high)//2
        # print(low, high, middle_point)
        if keys[middle_point] == query: 
            return middle_point
        # if the middle point is larger than query
        elif keys[middle_point] > query: 
            return helper(keys, low, middle_point-1, query)
        # if the middle point is smaller than query 
        else:
            return helper(keys, middle_point+1, high, query)
    else: 
        return -1 

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
