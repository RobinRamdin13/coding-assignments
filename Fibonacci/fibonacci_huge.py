def main(n:int, m:int)->int:
    """Function to compute the n-th Fibonacci modulo m

    Args:
        n (int): n-th Fibonacci number
        m (int): modulo

    Returns:
        int: mod of Fibonacci number
    """    
    # base case
    if n<= 1: return n

    # compute the pisano period for the mod 
    pisano = [0, 1]
    while True:
        # compute the fibanocci's mod 
        pisano.append((pisano[-2] + pisano[-1])%m)
        if pisano[-1] == 1 and pisano[-2] == 0: 
            break
    pisano = pisano[:-2]
    
    # get the mod
    pisano_len = len(pisano)
    remainder = n%pisano_len
    return pisano[remainder]

if __name__ == '__main__':
    input_text = list(map(int, input().split()))
    n , m = input_text[0], input_text[1]
    print(main(n, m))