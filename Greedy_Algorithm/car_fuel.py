from sys import stdin
from typing import List

def min_refills(distance:int, tank:int, stops:List)->int:
    """Function to compute the minimum number of gas tanks refills 
    to get from one city to another.

    Args:
        distance (int): total distance between two cities
        tank (int): distance covered on a full tank
        stops (List): list of potential gas stops

    Returns:
        int: minimum number of gas tanks refills
    """    
    # append the destination to the stops 
    stops.append(distance)

    # check if destination between stops is possible 
    if any(stops[i] - stops[i-1] > tank for i in range(1, len(stops))): return -1 

    # destination is possible 
    num_stops = 0 
    meter = 0 
    for i in range(1, len(stops)):
        if tank >= stops[i-1] - meter:
            if tank < stops[i] - meter: 
                num_stops += 1 # add a stop 
                meter = stops[i-1] # update the meter 
            elif tank == stops[i] - meter and stops[i] != distance: 
                num_stops += 1
                meter = stops[i]
    return num_stops

if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))