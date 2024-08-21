from typing import List

def main(n:int)->List:
    summands = [] 
    iter = 1
    while iter+1 <= n-iter: 
        # print(f'iter: {iter}, n: {n}')
        summands.append(iter)
        n -= iter
        iter += 1
        # print(f'updated iter: {iter}, updated n: {n}')
    if 0 < n: 
        # print('append')
        summands.append(n)
    return summands

if __name__ == '__main__':
    n = int(input())
    summands = main(n)
    print(len(summands))
    print(*summands)
