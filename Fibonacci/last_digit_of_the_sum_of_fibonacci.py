def main(n:int, mod=10)->int: 
    """Function to get the last digit of the sum of Fibonacci numbers

    Args:
        n (int): n-th Fibonacci number
        mod (int, optional): mod enables us to get the last digit. Defaults to 10.

    Returns:
        int: last digit of sum
    """    
    # compute the pisano period for the mod 
    pisano = [0, 1]
    while True:
        # compute the fibanocci's mod 
        pisano.append((pisano[-2] + pisano[-1])%mod)
        if pisano[-1] == 1 and pisano[-2] == 0: 
            break
    pisano_mod_10 = pisano[:-2]
    len_pisano_mod_10 = len_pisano_mod_10
    pisano_total = sum(pisano_mod_10) # summ all the numbers to get the total
    reaminder = n%len_pisano_mod_10 # find the reaminder for pisano index
    index = n//len_pisano_mod_10 # find the number of pisano period
    output_param = sum(pisano_mod_10[:reaminder]) + (pisano_total*index)%mod # compute the last digit of sum
    return output_param%mod

if __name__ == '__main__':
    n = input()
    print(main(int(n)+1))