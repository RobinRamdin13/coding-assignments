from sys import stdin
from typing import List
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def main(segments:List)->List:
    """Function to find the m

    Args:
        segments (List): list of Segments

    Returns:
        List: list of minimum points to connect all segments
    """    
    points = []
    while segments: 
        curr = compute_smallest_end(segments)
        points.append(curr)
        segments = reduce_segments(segments, curr)
    return points

def compute_smallest_end(segments:List)->int:
    """Function to compute the smallest segment end

    Args:
        segments (List): list of Segments

    Returns:
        int: smallest end value
    """    
    end = 10**9
    for s in segments:
        if s.end < end : end = s.end
    return end

def reduce_segments(segments:List, curr:int)->List:
    """Function to remove segments already covered by current point

    Args:
        segments (List): list of Segments
        curr (int): current point

    Returns:
        List: shortened list of Segments
    """    
    drop = []
    for x in segments:
        if x.start <= curr:
            drop.append(x)
    return [f for f in segments if f not in drop]

if __name__ == '__main__':
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = main(segments)
    print(len(points))
    print(*points)
