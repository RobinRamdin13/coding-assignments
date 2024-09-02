from typing import List
from collections import defaultdict

def majority_element_naive(elements:List)->int:
    half_criteria = len(elements)//2 + 1
    e_count = defaultdict(int)
    for e in elements: 
        e_count[e] += 1
        if e_count[e] == half_criteria:
            return 1 
    return 0


if __name__ == '__main__':
    input_n = int(input())
    input_elements = list(map(int, input().split()))
    assert len(input_elements) == input_n
    print(majority_element_naive(input_elements))
