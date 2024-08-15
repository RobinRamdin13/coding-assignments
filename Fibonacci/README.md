## Introduction
This folder contains individual scripts for different problem statements using Fibonacci sequence. External constraints were set on the space and time complexity to ensure the scripts run efficiently for very large inputs. The purpose of each of the scripts can be found in their function descriptions.
___

### Executing fibonacci.py
To run the main file run the following command within your terminal `python fibonacci.py`. Following which the program will wait for the user input:
- `n`: n-th Fibonacci number 

### Executing fibonacci_huge.py
To run the main file run the following command within your terminal `python fibonacci_huge.py`. Following which the program will wait for the user inputs:
- `n`: n-th Fibonacci number 
- `m`: modulo number

### Executing fibonacci_last_digit.py
To run the main file run the following command within your terminal `python fibonacci_last_digit.py`. Following which the program will wait for the user input:
- `n`: n-th Fibonacci number 

### Executing last_digit_of_sum_squares_of_fibonacci.py
To run the main file run the following command within your terminal `python last_digit_of_sum_squares_of_fibonacci.py`. Following which the program will wait for the user input:
- `n`: n-th Fibonacci number 

### Executing last_digit_of_the_sum_of_fibonacci.py
To run the main file run the following command within your terminal `python last_digit_of_the_sum_of_fibonacci.py`. Following which the program will wait for the user input:
- `n`: n-th Fibonacci number 

### Executing last_digit_partial_sum_of_fibonacci.py
To run the main file run the following command within your terminal `python last_digit_partial_sum_of_fibonacci.py`. Following which the program will wait for the user input:
- `m`: m-th Fibonacci number
- `n`: n-th Fibonacci number 

___

### Note:
Since we are using the pisano periods in most cases, the sum of the pisano for modulo 10 is equal to zero (i.e `sum(pisano_for_mod_10)%10 == 0`). When computing the product between number of pisano periods into the pisano total the product is always zero for modulo 10. This is also the case observed when using squared Fibonacci number. The logic was kept within the scripts to enable usage of other modulo.