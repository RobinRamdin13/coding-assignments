## Introduction
This folder contains individual scripts for different problem statements using Fibonacci sequence. External constraints were set on the space and time complexity to ensure the scripts run efficiently for very large inputs. The purpose of each of the scripts can be found in their function descriptions.

To ensure time and space complexity were met, **Pisano Periods** in most cases as opposed of naive approaches. Consider familiarizing yourself with this topic before going through the scripts for a better understanding.
___

### Executing python files
To run a file, run the following command within your terminal `python name_of_file`. Where `name_of_file` is to be substituted by the desired file name. 

### File inputs 
Different files require different number of inputs, I have consolidated all the inputs and a short description for each rescpective file here: 
- `fibonacci.py`&#8594; `n`: n-th Fibonacci number 
- `fibonacci_huge.py`&#8594; `n`: n-th Fibonacci number &  `m`: modulo number
- `fibonacci_last_digit.py`&#8594; `n`: n-th Fibonacci number 
- `last_digit_of_sum_squares_of_fibonacci.py`&#8594; `n`: n-th Fibonacci number 
- `last_digit_of_the_sum_of_fibonacci.py`&#8594; `n`: n-th Fibonacci number 
- `last_digit_partial_sum_of_fibonacci.py`&#8594; `m`: m-th Fibonacci number & `n`: n-th Fibonacci number 

### Time Complexity
Below are the time complexities for each of the scripts.
- `fibonacci.py`&#8594; O(n)
- `fibonacci_huge.py`&#8594; O(m)
- `fibonacci_last_digit.py`&#8594; O(n)
- `last_digit_of_sum_squares_of_fibonacci.py`&#8594; O(1)
- `last_digit_of_the_sum_of_fibonacci.py`&#8594; O(1)
- `last_digit_partial_sum_of_fibonacci.py`&#8594; O(1)
 
___

### Note:
Since we are using the pisano periods in most cases, the sum of the pisano for modulo 10 is equal to zero (i.e `sum(pisano_for_mod_10)%10 == 0`). When computing the product between number of pisano periods into the pisano total the product is always zero for modulo 10. This is also the case observed when using squared Fibonacci number. The logic was kept within the scripts to enable usage of other modulo.