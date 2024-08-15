
def main(n:int, mod=10)-> int:
    """Function to compute the last digit of the n-th Fibonacci number

    Args:
        n (int): n-th Fibonacci number
        mod (int, optional): mod enables us to extract the last digit. Defaults to 10.

    Returns:
        int: last digit of Fibonacci number 
    """
    n_1, n_2 = 0, 1 # instantiate the first two terms 
    # base case 
    if n <= 1: 
        if n == 1: return n_2
        if n == 0: return n_1
    else: 
        iter = 0 # set the iteration variable to 0
        while iter < n: 
            temp_n = n_2%mod # temporarily save the n_2 term
            n_2 = (n_1 + n_2)%mod # compute new term
            n_1 = temp_n # assign saved term to n_1
            iter += 1 # increment the iteration by 1
    return n_1%mod

if __name__ == '__main__':
    n = input()
    print(main(int(n)))