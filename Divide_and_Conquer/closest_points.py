from collections import namedtuple
from math import sqrt


Point = namedtuple('Point', 'x y')

def distance_squared(first_point, second_point):
    return (first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2

def minimum_distance_squared(points):
    points.sort(key=lambda point: point.x)
    return recursion(points)

def check_points(temp_points, min_dist):
    len_temp_points = len(temp_points)
    # iterate through each points
    for i in range(len_temp_points):
        j = i + 1 # iterator for next point
        while j < len_temp_points and abs(i-j) < 7:
            # compute the minimum value and update existing 
            min_dist = min(distance_squared(temp_points[i], temp_points[j]), min_dist)
            j += 1# increment the j counter
    return min_dist

def recursion(points, min_dist = float('inf')):
    points_len = len(points)
    # base case to end recursion 
    if points_len == 1: 
        return min_dist # we cant compute a line with a single point
    # if two points exist compute their distance
    elif points_len == 2: 
        return distance_squared(points[0], points[1])
    # if three points exist compute their distance
    elif points_len == 3: 
        return min(distance_squared(points[0], points[1]), distance_squared(points[0], points[2]), distance_squared(points[1], points[2]))
    
    # split x coordinate into two segments
    mid_point = (points_len+1)//2
    left, mid, right = points[:mid_point], points[mid_point], points[mid_point:]

    # trigger recursion to find minimum between two segments
    min_dist = min(recursion(left), recursion(right))

    # remove points which greater than min_dist from mid point 
    temp_points = [f for f in points if abs(f.x - mid.x) < min_dist]

    # sort the remaining points on their y coordinates
    temp_points.sort(key= lambda point: point.y)

    return min(min_dist, check_points(temp_points, min_dist))


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)

    print("{0:.9f}".format(sqrt(minimum_distance_squared(input_points))))
