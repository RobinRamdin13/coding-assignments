from typing import List

def max_dot_product(first_sequence:List, second_sequence:List)->int:
    """Function to compute the maximum dot product of two sequences
    of numbers

    Args:
        first_sequence (List): first sequence
        second_sequence (List): second sequence

    Returns:
        int: dot product
    """    
    # sort the respective lists
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)
    product = [a*b for a,b in zip(first_sequence, second_sequence)]
    return sum(product)


if __name__ == '__main__':
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
    
