def find_sum(n):
    if n==1:
        return 1
    return n + find_sum(n-1)

def fib(n):
    # 0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index
    if n==0 or n==1:
        return n
    return fib(n-1) + fib(n-2)

# print(find_sum(5))
# print(fib(10))

# 1. Write a Python program to calculate the sum of a list of numbers using recursion.
# Click me to see the sample solution

def find_list_sum(list):
    if len(list) == 0:
        return 0
    if len(list) == 1:
        return list[0]
    return list[len(list)-1] + find_list_sum(list[0:len(list)-1])

# print(find_list_sum([4,2,3,8,13,10,10]))

# 2. Write a Python program to convert an integer to a string in any base using recursion .
# Click me to see the sample solution

#IDK what that means

# 3. Write a Python program to sum recursion lists using recursion.
# Test Data: [1, 2, [3,4], [5,6]]
# Expected Result: 21
# Click me to see the sample solution

def find_list_of_lists_sum(list):
    for item in list:
        if type(item) == int:
            return item
        elif type(item) == list:
            find_list_of_lists_sum(item)
    return 

# print(find_list_of_lists_sum([1, 2, [3,4], [5,6]]))

# 4. Write a Python program to get the factorial of a non-negative integer using recursion.
# Click me to see the sample solution

def find_factorial(int):
    if int == 0 or int ==1:
        return 1
    return int * find_factorial(int-1)

# print(find_factorial(6))

# 5. Write a Python program to solve the Fibonacci sequence using recursion.
# Click me to see the sample solution

def fib2(n):
    # 0,1,1,2,3,5,8 <-- fibonacci numbers
    # --------------
    # 0,1,2,3,4,5,6 <-- index
    if n==0 or n==1:
        return n
    return fib2(n-1) + fib2(n-2)

# print(fib(7))

# 6. Write a Python program to get the sum of a non-negative integer using recursion.
# Test Data:
# sumDigits(345) -> 12
# sumDigits(45) -> 9
# Click me to see the sample solution

def sumDigits(number):
    str_num = str(number)
    digits = [int(num) for num in str_num]

    if len(digits) == 0:
        return 0
    if len(digits) == 1:
        return int(digits[0])
    
    updated_list = digits[:-1]
    str_digits = ''.join(str(digit) for digit in updated_list)
    new_number = int(str_digits)
    return int(digits[len(digits)-1]) + sumDigits(new_number)

# print(sumDigits(345))


# 7. Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0) using recursion .
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30
# Click me to see the sample solution

def sum_minus_twos(num):
    if num == 0 or num == 1 or num == 2:
        return num
    return num + sum_minus_twos(num-2)

# print(sum_minus_twos(15))
    

# 8. Write a Python program to calculate the sum of harmonic series upto n terms.
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# harmonic series
# Click me to see the sample solution

def harmonic_sum(num):
    if num == 0:
        return "n/a"
    if num == 1:
        return 1
    return (1/num) + harmonic_sum(num-1)

# print(harmonic_sum(5))

# 9. Write a Python program to calculate the geometric sum up to 'n' terms.
# Note: In mathematics, a geometric series is a series with a constant ratio between successive terms.

# Ex: geometric_sum(3) = 1+ 1/2 + 1/4

def geometric_sum(num):
    if num == 0:
        return 1
    return 1/(pow(2,num)) + geometric_sum(num-1)

# print(geometric_sum(4))

# Click me to see the sample solution

# 10. Write a Python program to calculate the value of 'a' to the power of 'b' using recursion.
# Test Data :
# (power(3,4) -> 81
# Click me to see the sample solution

def calc_exponent(a,b):
    if b == 1:
        return a
    return a * calc_exponent(a,b-1)

# print(calc_exponent(4,3))

# 11. Write a Python program to find the greatest common divisor (GCD) of two integers using recursion.
# Click me to see the sample solution

def Recurgcd(a, b):
    # Determine the lower and higher values between 'a' and 'b'
    low = min(a, b)
    high = max(a, b)

    # Check if the lower value is 0 (base case for GCD calculation)
    if low == 0:
        # If the lower value is 0, return the higher value (GCD is the non-zero value)
        return high
    # Check if the lower value is 1 (base case for GCD calculation)
    elif low == 1:
        # If the lower value is 1, return 1 (GCD of any number with 1 is 1)
        return 1
    else:
        # If neither base case is met, recursively call the Recurgcd function
        # with the lower value and the remainder of the higher value divided by the lower value
        return Recurgcd(low, high % low)

# Print the result of calling the Recurgcd function with the input values 12 and 14
print(Recurgcd(24, 64))


def find_GCF(a,b):
    if a % b == 0: #if b is divisible by a
        return b
    if b%a == 0: #if a is divisible by b
        return a
    
    factors_a = []
    for i in range (1,a+1):
        if a % i == 0:
            factors_a.append(i)
    
    factors_b = []
    for i in range (1,b+1):
        if b % i == 0:
            factors_b.append(i)

    common_factors = []

    if len(factors_a) < len(factors_b): #use the shorter list to save run time
        for factor in factors_a:
            if factor in factors_b:
                common_factors.append(factor)
    else:
        for factor in factors_b:
            if factor in factors_a:
                common_factors.append(factor)

    return max(common_factors)
            
print(find_GCF(24,64))
print(find_GCF(24,16))