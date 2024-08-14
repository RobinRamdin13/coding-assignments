
def get_gcd(num1:int, num2:int)->int: 
    if num2 == 0: 
        return num1
    else: 
        return get_gcd(num2, num1%num2)


if __name__ == '__main__':
    input_nums = input().split()
    num1, num2 = int(input_nums[0]), int(input_nums[1])
    print(get_gcd(num1, num2))