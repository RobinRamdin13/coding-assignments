

def main(numb:int)->int:
    """Function to compute the minimum number of coins needed
    to change the input value into coins with denominations of
    $0.01, $0.05 and $0.10.

    Args:
        numb (int): input number

    Returns:
        int: minimum number of coins required to satisfy the 
        input number
    """    
    return (numb//10) + (numb%10)//5 + (numb%10)%5


if __name__ == '__main__':
    input_text = int(input())
    print(main(input_text))