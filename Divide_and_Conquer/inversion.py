from typing import List
from itertools import combinations


def inversions_naive(a):
    number_of_inversions = 0
    for i, j in combinations(range(len(a)), 2):
        if a[i] > a[j]:
            number_of_inversions += 1
    return number_of_inversions

def inversions(a:List, numb_inversion = 0): 
    # base case when a contains one element 
    if len(a) <= 1: return a, numb_inversion

    # instantiate the mid point
    mid_point = len(a)//2
    left, right = a[:mid_point], a[mid_point:] # split into left and right side

    (sorted_left, numb_inversion1) = inversions(left, numb_inversion)
    (sorted_right, numb_inversion2) = inversions(right, numb_inversion)
    numb_inversion = numb_inversion1 + numb_inversion2
    a, numb_inversion = merge(sorted_left, sorted_right, numb_inversion)
    return a, numb_inversion

def merge(left_side, right_side, numb_inversion): 
    output = []
    left_count, right_count = 0, 0 

    while left_count < len(left_side) and right_count < len(right_side):
        # numbers are in ascending order
        if left_side[left_count] <= right_side[right_count]:
            output.append(left_side[left_count])
            left_count += 1
        else: 
            # numbers are not in ascending order
            output.append(right_side[right_count])
            numb_inversion += (len(left_side) - left_count)
            right_count += 1


    # add the remainding left side first followed by right side 
    output.extend(left_side[left_count:])
    output.extend(right_side[right_count:])
    return output, numb_inversion

def orchestrator(a:List):
    a, numb_inversion = inversions(a)
    return numb_inversion

if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    print(orchestrator(elements))
