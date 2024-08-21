import os
import random

def main(): 
    while True: 
        # generate the car fuel input data for stress testing 
        distance = random.randint(1,10**5 + 1)
        tank = random.randint(1, 400 + 1)
        num_of_stops = random.randint(1, 300 + 1)
        stops = random.sample(range(distance), num_of_stops)
        stops.sort() # sort in ascending order 
        stops = " ".join(map(str, stops)) # format the stops into required format
        output = f"{distance}\n{tank}\n{num_of_stops}\n{stops}\n"
        with open('car_fuel_test.txt', 'w') as text_file:
            text_file.write(output)
        
        os.system(f"python car_fuel.py < car_fuel_test.txt")                                                        
    return 

if __name__ == '__main__':
    main()