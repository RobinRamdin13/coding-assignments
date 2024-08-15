
def main(n:int)-> None:
    """Compute the fibonacci number for the nth term

    Args:
        n (int): nth term in fibonacci 
    """   
    n_1, n_2 = 0, 1 # instantiate the first two terms 
    # base case 
    if n <= 1: 
        if n == 1: return n_2
        if n == 0: return n_1
    else: 
        iter = 0 # set the iteration variable to 0
        while iter < n: 
            temp_n = n_2 # temporarily save the n_2 term
            n_2 = n_1 + n_2 # compute new term
            n_1 = temp_n # assign saved term to n_1
            iter += 1 # increment the iteration by 1
    return n_1

if __name__ == '__main__':
    n = input()
    print(main(int(n)))