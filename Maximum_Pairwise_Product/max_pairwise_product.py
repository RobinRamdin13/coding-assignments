import time
from typing import List

def max_pairwise_product_fast(numbers:List)-> int:
    """Compute the maximum product between two elements of a list

    Args:
        numbers (List): List containing elements

    Returns:
        int : product of elements
    """    
    param_max, param_next_max = 0, 0 # instantiate the params to hold the two largest values
    index = 0 # instantiate the index variable 
    while index < len(numbers):
        value = numbers[index] # instantiate the current value
        
        # new number is greater than param max
        if value >= param_max:
            param_next_max = param_max
            param_max = value
        
        # new number is greater than param next max but less than param max
        elif value > param_next_max:
            param_next_max = value
        
        index += 1 # increment the index
    return param_max * param_next_max

if __name__ == '__main__':
    # run the logic
    input_numbers = list(map(int, input().split()))
    start = time.process_time()
    print(max_pairwise_product_fast(input_numbers))
    end = time.process_time()
    print(f'Function Run Time: {end - start}')
  

