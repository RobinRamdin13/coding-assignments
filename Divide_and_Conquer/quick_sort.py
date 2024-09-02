from random import randint
from typing import List, Tuple

def partition3(array:List, left:int, right:int)->Tuple[int, int]:
    x = array[left]
    less, more = left, right
    i = left
    while i <= more: 
        # value is less than x
        if array[i] < x: 
            array[less], array[i] = array[i], array[less]
            less += 1 
        # value is more than x
        elif array[i] > x:
            array[more], array[i] = array[i], array[more]
            more -= 1
            i -= 1
        # increment the iterator
        i += 1
    return less, more

def randomized_quick_sort(array:List, left:int, right:int):
    if left >= right:
        return array
    k = randint(left, right)
    array[left], array[k] = array[k], array[left]
    m1, m2 = partition3(array, left, right)
    randomized_quick_sort(array, left, m1 - 1)
    randomized_quick_sort(array, m2 + 1, right)


if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    randomized_quick_sort(elements, 0, len(elements) - 1)
    print(*elements)

