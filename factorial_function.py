def factorial(num):
    result = 1
    if num < 0:
        raise ValueError
    while num > 0:
        result *= num
        num -= 1
    return result