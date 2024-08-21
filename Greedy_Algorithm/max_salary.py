from typing import List

def remove_numb(numbers:List, number:str)->List:
    """Function to remove a number from a list, without removing
    the duplicates

    Args:
        numbers (List): given list
        number (str): number to remove

    Returns:
        List: _description_
    """    
    for i in range(len(numbers)): 
        if numbers[i] == number: 
            numbers.pop(i)
            return numbers

def main(numbers:List)->str:
    """Function to compile the largest integer by concatenating
    the given integers

    Args:
        numbers (List): list of given integers

    Returns:
        str: largest integer
    """    
    output = ''
    while numbers: 
        max_value = numbers[0]
        for numb in numbers[1:]: 
            # numbers of same length
            if len(numb) == len(max_value):
                if int(numb) >= int(max_value): 
                    max_value = numb
            else: 
                if int(numb+max_value) > int(max_value+numb):
                    max_value = numb
        output += max_value
        numbers = remove_numb(numbers, max_value)
    return output

if __name__ == '__main__':
    _ = int(input())
    input_numbers = input().split()
    print(main(input_numbers))
