def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False



def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False



def factorial(number):
    if number < 0:
        return "invalid number"
    elif number == 0:
        return 1
    else:
        result = 1
        for num in range(1, number + 1):
            result *= num
        return result

            