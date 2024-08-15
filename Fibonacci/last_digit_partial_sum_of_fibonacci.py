
def main(m:int, n:int, mod:int = 10)->int:
    """Function to get the last digit from the sum of Fibonacci numbers
    from m-th to the n-th term.

    Args:
        m (int): m-th term
        n (int): n-th term
        mod (int, optional): mod enables us to extract the last digit. Defaults to 10.

    Returns:
        int: last digit from sum
    """    
    # base case
    if n==m==0: return 0 
    
    # generate pisano period range for mod 
    pisano = [0, 1]
    while True:
        # compute the fibanocci's mod 
        pisano.append((pisano[-2] + pisano[-1])%mod)
        if pisano[-1] == 1 and pisano[-2] == 0: 
            break
    pisano = pisano[:-2]
    l_pisano = len(pisano)
    total_pisano = sum(pisano)%mod
    # instantiate the start and end index for the pisano period
    start_index, start_remainder = m//l_pisano, m%l_pisano
    end_index, end_remainder = n//l_pisano, n%l_pisano 

    # compute the output
    if end_remainder >= start_remainder:
        output = (end_index-start_index)*total_pisano + sum(pisano[start_remainder:end_remainder+1])%mod 
    else: 
        output = (end_index-start_index)*total_pisano + sum(pisano[start_remainder:])%mod + sum(pisano[:end_remainder+1])%mod
    return output%mod

if __name__ == '__main__':
    input_text = list(map(int, input().split()))
    m , n = input_text[0], input_text[1]
    print(main(m, n))