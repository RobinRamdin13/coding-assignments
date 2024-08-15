def get_gcd(num1:int, num2:int)->int:
    """Function to get the greatest common divisor between two integers

    Args:
        num1 (int): first integer
        num2 (int): second integer

    Returns:
        int: greatest common divisor
    """    
    if num2 == 0: 
        return num1
    else: 
        return get_gcd(num2, num1%num2)

def get_lcm(num1:int, num2:int)->int:
    """Function to get the least common multiple between two integers

    Args:
        num1 (int): first integer
        num2 (int): second integer

    Returns:
        int: least common multiple
    """    
    return int((num1*num2)/get_gcd(num1, num2))

if __name__ == '__main__':
    input_nums = input().split()
    num1, num2 = int(input_nums[0]), int(input_nums[1])
    print(get_lcm(num1, num2))