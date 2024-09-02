from sys import stdin
from typing import List
from bisect import bisect_left, bisect_right

def points_cover_fast(starts:List, ends:List, points:List): 
    starts.sort()
    ends.sort()
    output = []
    for point in points: 
        right = bisect_right(starts, point)
        left = bisect_left(ends, point)
        count = right - left 
        output.append(count)
    return output

if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover_fast(input_starts, input_ends, input_points)
    print(*output_count)
