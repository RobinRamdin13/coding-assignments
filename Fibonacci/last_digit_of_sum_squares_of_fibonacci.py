def main(n:int, mod=10)->int:
    """Function to return the last digit of the sum of squares
    of Fibonacci numbers

    Args:
        n (int): n-th Fibonacci number
        mod (int, optional): mod enables us to extract the last digit. Defaults to 10.

    Returns:
        int: last digit of sum of squares of Fiboacci number
    """    
    # base case
    if n<= 1: return n

    # compute the pisano period for the mod 
    pisano = [0, 1]
    while True:
        # compute the fibanocci's mod 
        pisano.append((pisano[-2] + pisano[-1])%mod)
        if pisano[-1] == 1 and pisano[-2] == 0: 
            break
    pisano = pisano[:-2]

    # transform the pisano list pisano squared 
    pisano = [(x**2)%mod for x in pisano]

    # extract the indexes and remainders
    pisano_len = len(pisano)
    total = sum(pisano)%mod
    index = n//pisano_len
    remainder = n%pisano_len

    # compute the sum
    output = (index*total)%mod + sum(pisano[:remainder+1])%mod
    return output%mod

if __name__ == '__main__':
    input_text = list(map(int, input().split()))
    n = input_text[0]
    print(main(n))