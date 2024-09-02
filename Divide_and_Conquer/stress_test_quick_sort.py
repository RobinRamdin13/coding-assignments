import os
import random
import subprocess
from random import randint

def main(): 
    while True: 
        # generate the random array size for quick sort algorithm
        n = randint(1, 10**2)
        array = random.sample(range(1,10**3), n)
        str_array = " ".join(map(str, array)) # format the stops into required format
        output = f"{n}\n{str_array}"
        with open('quick_sort_test.txt', 'w') as text_file:
            text_file.write(output)
        os.system(f"python quick_sort.py < quick_sort_test.txt")
    return 

if __name__ == '__main__':
    main()