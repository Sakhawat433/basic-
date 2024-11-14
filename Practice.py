import math

# Example numbers
x = -3.7
n = 5
base = 2
exp = 3
sqrt_num = 16
log_num = 10

# Using math functions
ceil_result = math.ceil(x)               # Ceiling of x
floor_result = math.floor(x)             # Floor of x
absolute_result = abs(x)                 # Absolute value of x
factorial_result = math.factorial(n)     # Factorial of n
power_result = math.pow(base, exp)       # base raised to the power exp
sqrt_result = math.sqrt(sqrt_num)        # Square root of sqrt_num
log_result = math.log(log_num)           # Natural log of log_num

# Print results
print("Ceil of", x, ":", ceil_result)
print("Floor of", x, ":", floor_result)
print("Absolute of", x, ":", absolute_result)
print("Factorial of", n, ":", factorial_result)
print(base, "to the power of", exp, ":", power_result)
print("Square root of", sqrt_num, ":", sqrt_result)
print("Natural log of", log_num, ":", log_result)
print(math.gamma(x))