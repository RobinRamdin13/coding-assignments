import random

input_text = input().split()
n, max_numb, seed = int(input_text[0]), int(input_text[1]), int(input_text[2])
random.seed(seed)

numbers = " ".join([str(random.randint(1, max_numb)) for i in range(n)])
output = str(n) + '\n' + str(numbers)
with open('input.txt', 'w') as text_file:
    text_file.write(output)